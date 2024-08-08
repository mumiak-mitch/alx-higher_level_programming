#!/usr/bin/python3
import sys
import requests

def main():
    # Get URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Send POST request with the email parameter
    response = requests.post(url, data={'email': email})

    # Print the body of the response
    print(response.text)

if __name__ == "__main__":
    main()

