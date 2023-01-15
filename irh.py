import requests
from requests.exceptions import RequestException

def send_request(url, method='GET', data=None, headers=None):
    try:
        if method == 'GET':
            response = requests.get(url, timeout=5)
        elif method == 'POST':
            response = requests.post(url, data=data, headers=headers, timeout=5)
        elif method == 'PUT':
            response = requests.put(url, data=data, headers=headers, timeout=5)
        elif method == 'DELETE':
            response = requests.delete(url, timeout=5)
        else:
            raise ValueError(f"Invalid method: {method}")
        # Raise an exception for non-200 status codes
        response.raise_for_status()
        return response
    except RequestException as e:
        print(f'Error: {e}')
    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("Something Else:",err)

# Get the URL, method, data and headers from the user
url = input("Enter the URL to send a request to: ")
method = input("Enter the request method (GET, POST, PUT, DELETE): ")
data = input("Enter the request data (if any): ")
headers = input("Enter the request headers (if any): ")

# Send the request and store the response
response = send_request(url, method=method, data=data, headers=headers)

# Save the response to a file
if response:
    with open('response.txt', 'w') as f:
        f.write(response.content)
        print(f"Response saved to response.txt")
