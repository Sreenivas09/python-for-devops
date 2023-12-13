import requests

response = requests.get(f'https://api.github.com/repos/kubernetes/kubernetes/pulls')
if response.status_code == 200:
    pull_requests = response.json()

for pull_request in pull_requests:
    data = pull_request['user']['login']
    data1 = pull_request['user']['id']  
    data2 = pull_request['created_at']  
    print(data, data1, data2)
