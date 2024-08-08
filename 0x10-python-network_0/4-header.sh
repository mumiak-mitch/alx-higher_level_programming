#!/bin/bash

# Check if a URL is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

URL="$1"

# Print the URL being requested
echo "Requesting URL: $URL"

# Send a GET request to the provided URL with the required header
response=$(curl -s -w "%{http_code}" -o response_body.txt -H "X-School-User-Id: 98" "$URL")

# Print the HTTP status code
echo "HTTP Status Code: $response"

# Check if response body file exists
if [ -f response_body.txt ]; then
  # Print the response body
  cat response_body.txt
else
  echo "No response body received."
fi

