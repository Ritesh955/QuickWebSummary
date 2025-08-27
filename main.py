import sys
from utils import display_summary

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <URL>")
        return
    url = sys.argv[1]
    try:
        display_summary(url)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()