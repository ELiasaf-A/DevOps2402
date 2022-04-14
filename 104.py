import requests
requests = requests.get('http://192.168.54.110:5001/whatismyname')
expected ="saved new car"
actual = requests.text
assert expected == actual
print(requests.text)


