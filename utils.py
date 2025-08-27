from website import Website

import requests

OLLAMA_API_URL = 'http://localhost:11434/v1/chat/completions'

def summarize(website, model='llama3.2'):
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You are an assistant that analyzes the contents of a website "
                           "and provides a short summary, ignoring navigation related text."
            },
            {
                "role": "user",
                "content": f"You are looking at a website titled '{website.title}'. "
                           f"The contents of this website are as follows:\n\n{website.text}\n\n"
                           "Please provide a concise summary, including any news or announcements, "
                           "and contact details if available."
            }
        ]
    }
    response = requests.post(OLLAMA_API_URL, json=payload, headers=headers)
    response.raise_for_status()
    result = response.json()
    return result['choices'][0]['message']['content']

def display_summary(url):
    """
    Fetches the webpage and displays the summary.
    """
    website = Website(url)
    summary = summarize(website)
    print(f"Title: {website.title}\n")
    print("Summary:\n")
    print(summary)