# Simple LangGraph Agent

This project demonstrates the implementation of a reactive agent using LangGraph, LangChain, and Groq's LPU™ (Language Processing Unit) for fast AI inference.

## Overview

This project showcases how to build a reactive agent that can process and respond to inputs using LangGraph's workflow management capabilities, combined with LangChain's components and Groq's high-performance inference.

## Prerequisites

- Python 3.9 or higher
- Virtual environment (recommended)
- Groq API key (for using Groq's LPU)
- OpenAI API key (for using OpenAI models)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd simple-langgraph-agent
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your environment variables:
```bash
export GROQ_API_KEY=your_groq_api_key
export OPENAI_API_KEY=your_openai_api_key
```

## Project Structure

- `simple-react-agent.py`: Main implementation of the reactive agent
- `requirements.txt`: Project dependencies
- `README.md`: Project documentation

## Dependencies

The project relies on the following main packages:
- `langgraph`: For creating and managing the agent's workflow
- `langchain-openai`: For OpenAI integration
- `langchain-groq`: For Groq integration

## Usage

[Usage instructions will be added once the agent implementation is complete]

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

[Add your chosen license]

## Acknowledgments

- LangChain team for providing the framework
- Groq for their high-performance LPU technology
- OpenAI for their language models
