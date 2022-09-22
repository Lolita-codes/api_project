import requests


headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYzODcyMDMyLCJpYXQiOjE2NjM4NjkyNTIsImp0aSI6IjU4MWYxNWRiY2U1YjQ5N2Q4M2UyOWE2MjhmNzEyYjNiIiwidXNlcl9pZCI6MX0.7WJBl6IXR1tm2riQNGkLxRCmVaLIS_yGIJvqymWiB58'

response = requests.get('http://127.0.0.1:8000/paradigms', headers=headers)

print(response.text)
