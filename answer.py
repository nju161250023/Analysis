import json
import  operator

f = open('group.json', encoding='utf-8')

res = f.read()
data = json.loads(res)
result = {}

print("Please enter your id")
user_id = input()
print("How many friends do you want?")
index = int(input())

friend = data[user_id]["friend"]

for i in friend:
    result.update(dict(i))

print(sorted(result, key=lambda x: result[x])[-index:])

