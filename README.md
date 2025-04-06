# Model Context Protocol Agent (More Protocol Agent)

## Overview

The **Protocol Agent** is a tool designed to streamline the process of analyzing open pull requests on GitHub. By leveraging AI models like OpenAI or Claude, the MCP Agent impersonates a software engineer to provide detailed insights, identify potential issues, assess impacts, and summarize pull requests.





## Features

- **Pull Request Metadata Extraction**: Automatically fetches metadata from open pull requests on GitHub.
- **AI-Powered Analysis**: Sends the metadata to an MCP Client (OpenAI or Claude) for intelligent analysis.
- **Engineer-Like Summaries**: Generates summaries that mimic the thought process of a software engineer.
- **Issue and Impact Identification**: Highlights potential issues and evaluates the impact of the changes.
- **Output to Notepad**: Outputs the analysis and summary to a `.txt` file for easy access.

## Use Case

This tool is ideal for teams looking to automate the review process of pull requests, saving time and ensuring a thorough analysis of changes. While the current implementation outputs results to a `.txt` file, future iterations could integrate with platforms like Notion for enhanced collaboration.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/karan-manhas/model_context_protocol_mvp.git
    ```
2. Navigate to the project directory:
    ```bash
    cd model_context_protocol_mvp
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have the necessary API keys for GitHub and the MCP Client (OpenAI or Claude).
2. Set the config in `github_integration.py`  
3. Run the MCP Agent:
    ```bash
    python pr_analyser_openai.py
    ```
4. The tool will fetch open pull requests, analyze them, and output the results to a `.txt` file.

## Prequisites

- Open PR on a repo on Github (Ensure to use PR NUMBER)
- OpenAI API key 



## Acknowledgments

- [OpenAI](https://openai.com/) and [Claude](https://www.anthropic.com/) for their powerful AI models.
- The open-source community for their invaluable tools and libraries.
## Setting Up a Python Virtual Environment

To ensure a clean and isolated environment for your project, it's recommended to use a Python virtual environment. Below are the steps for setting up a virtual environment on Windows, Linux, and macOS.

### Windows

1. Open a terminal or command prompt.
2. Navigate to your project directory:
    ```bash
    cd c:/Users/Karan/repos/mcp_mvp
    ```
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    ```bash
    venv\Scripts\activate
    ```
5. To deactivate the virtual environment, run:
    ```bash
    deactivate
    ```

### Linux and macOS

1. Open a terminal.
2. Navigate to your project directory:
    ```bash
    cd /path/to/mcp_mvp
    ```
3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```
5. To deactivate the virtual environment, run:
    ```bash
    deactivate
    ```

Once the virtual environment is activated, you can proceed to install the project dependencies using:
```bash
pip install -r requirements.txt
```