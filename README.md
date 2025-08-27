# QuickWebSummary
A Python-based tool that fetches webpage content, extracts the main text, and g enerates concise summaries using local AI models like Ollama 3.2. Designed to help users quickly grasp the key points of any webpage without manual reading. Ideal for researchers, content curators, and anyone looking to save time by automating webpage summarization.
This project fetches a webpage, extracts its content, and generates a short summary, ignoring navigation-related text.

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`

## Setup

1. Clone the repository:

    ```bash
    git clone git@github.com:Ritesh955/QuickWebSummary.git
    cd QuickWebSummary
    ```

2. Create a virtual environment (optional but recommended):

    `python -m venv venv`

    `source venv/bin/activate` 

3. Install dependencies:

    `pip install -r requirements.txt`

4. Ensure Ollama 3.2 is installed and running locally at http://localhost:11434.
   Follow Ollama's installation instructions: [Ollama Documentation](https://ollama.com/)

   
5. Usage
   Run the script with the URL you want to analyze:

    ```python main.py https://example.com```

6. Examples:

    ```python main.py "https://cnn.com"```

     ![Screenshot 2025-08-27 at 4.45.24 PM.png](Screenshot%202025-08-27%20at%204.45.24%E2%80%AFPM.png)
    
    ```python main.py "https://scotiabank.com"```

     ![Screenshot 2025-08-27 at 4.46.37 PM.png](Screenshot%202025-08-27%20at%204.46.37%E2%80%AFPM.png)
