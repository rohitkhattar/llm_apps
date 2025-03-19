import getpass
import os
from langchain_openai import ChatOpenAI
from typing import Annotated
from langchain_groq import ChatGroq


# Importing TypedDict from typing_extensions for type hinting
from typing_extensions import TypedDict

# Importing StateGraph, START, and END from langgraph.graph
from langgraph.graph import StateGraph, START, END

# Importing add_message from langgraph.graph.message, its a reducer function
from langgraph.graph.message import add_messages

# Importing HumanMessage and SystemMessage from langchain_core.messages
from langchain_core.messages import HumanMessage, SystemMessage

# Creating a private function to set the environment variable if it is not 
# already set, using getpass to ensure the input is not visible to others
def _set_env(var: str):
    """
    Sets the environment variable specified by 'var'.

    If the environment variable is not already set, it prompts the user to 
    enter a value for the variable using getpass to ensure the input is 
    not visible.

    Args:
        var (str): The name of the environment variable to set.
    """
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"Enter your {var}: ")
    else:
        print(f"{var} already set")

# Invoking the _set_env function to set the OPENAI_API_KEY environment 
# variable
_set_env("OPENAI_API_KEY")
_set_env("GROQ_API_KEY")

# Creating a class for the AgentState, which inherits from TypedDict
# with one key: messages
#  The add_messages reducer function is used to append new messages to the list instead of overwriting it. 
# Keys without a reducer annotation will overwrite previous values.
class AgentState(TypedDict):
    # Messages have the type "list". The add in the annotation defines how 
    # this state key should be updated (in this case, it appends messages 
    # to the list, rather than overwriting it)
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(AgentState)

# Notes: The graph can now handle two key tasks:
# 1. Each node can receive the current State as input and output an update 
# to the state. 
# 2. Updates to messages will be appended to the existing list 
# rather than overwriting it, thanks to the prebuilt add_messages function 
# used with the Annotated syntax.

#llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.environ["OPENAI_API_KEY"])
llm = ChatGroq(model_name="llama3-70b-8192", api_key=os.environ["GROQ_API_KEY"])

def chatbot(state: AgentState):
    return {"messages": [llm.invoke(state["messages"])]}

# The first argument is the unique node name
# The second argument is the function or object that will be called whenever 
# the node is used.

graph_builder.add_node("chatbot", chatbot)

# Adding an edge from the START node to the chatbot node
graph_builder.add_edge(START, "chatbot")

# Adding an edge from the chatbot node to the END node
graph_builder.add_edge("chatbot", END)

# Creating a graph from the graph_builder object. 
# This creates a compiled graph object that can be used to 
# invoke the graph on the input state.
graph = graph_builder.compile()

def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [HumanMessage(content=user_input)]}):
        for value in event.values():
            print("Assistant: ", value["messages"][-1].content)

while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit", "q"]:
            print("Goodbye!")
            break
        
        stream_graph_updates(user_input)
    except:
        # fallback if inpuut is not available
        user_input = "What do you know about LangGraph?"
        print("User: ", user_input)
        stream_graph_updates(user_input)
        break