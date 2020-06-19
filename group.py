import json

f = open('flag.json', encoding='utf-8')

res = f.read()
data = json.loads(res)
goal = {}

for key1 in data:
    res1 = []
    list1 = data[key1]

    for key2 in data:
        res2 = []
        list2 = data[key2]
        for i in range(len(list1)):
            res2.append(list1[i] ^ list2[i])
        target = {key2: res2.count(1)}
        res1.append(target)

    print(res1)
    goal[key1] = {"friend": res1}

json_str = json.dumps(goal, indent=4, ensure_ascii=False)

with open("G:\python\Analysis"+"\\"+"group.json", 'w', encoding='utf-8') as json_file:
    json_file.write(json_str)