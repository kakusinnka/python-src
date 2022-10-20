import requests
# request
res = requests.get('http://127.0.0.1:8090/user')

print(type(res)) # <class 'requests.models.Response'>
print(res) # <Response [200]>
print("----------------------------")

print(type(res.text)) # <class 'str'>
print(res.text) # {"name":"laoliu","id":"123456","studentDto":{"classes":"sanban","studentId":"202020"}}
print("----------------------------")

print(type(res.json())) # <class 'dict'>
print(res.json()) # {'name': 'laoliu', 'id': '123456', 'studentDto': {'classes': 'sanban', 'studentId': '202020'}}
print("----------------------------")

print(res.json().get("name")) # laoliu
print(res.json().get("studentDto").get("classes")) # sanban
print("----------------------------")

input("please input.")