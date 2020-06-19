import json

fs = open("G:\python\Analysis"+"\\"+'score.json', encoding='utf-8')
ft = open("G:\python\Analysis"+"\\"+'template.json', encoding='utf-8')

res1 = fs.read()
data = json.loads(res1)
res2 = ft.read()
template = json.loads(res2)

scoreKey = []
templateKey = template.keys()
goal = {}

for key in data:
    user_id = str(key)
    cases = data[key]['cases']
    cid = []
    res = []

    for case in cases:
        if case["score"] == 100:
            cid.append(case['case_id'])

    for i in templateKey:
        if i in cid:
            res.append(1)
        else:
            res.append(0)

    goal[user_id] = res

json_str = json.dumps(goal, indent=4, ensure_ascii=False)

with open("G:\python\Analysis"+"\\"+"flag.json", 'w', encoding='utf-8') as json_file:
    json_file.write(json_str)