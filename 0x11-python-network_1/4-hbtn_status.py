#!/usr/bin/python3
import requests

def main():
    # Fetch the URL
    response = requests.get('https://alx-intranet.hbtn.io/status')

    # Extract response content
    content = response.text

    # Display the response body in the specified format
    print("Body response:")
    print(f"    - type: {type(content)}")
    print(f"    - content: {content}")

if __name__ == "__main__":
    main()

