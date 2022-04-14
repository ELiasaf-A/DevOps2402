import requests

requests = requests.get("https://api.github.com/users/avielb/repos")
# if requests.status_code ==200:
#     print("github is up and running")
# print(requests.text)
print(requests.json())
for repo in requests.json():
    print(repo["full_name"])
