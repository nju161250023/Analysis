import json

f = open('test_data.json', encoding='utf-8')

res = f.read()
data = json.loads(res)
users = {}

for key in data:
    cases = data[key]['cases']
    user_id = str(data[key]['user_id'])
    newCases = []
    print(user_id)
    print(cases)

    for case in cases:
        newCase = {"case_id": case["case_id"],
                   "case_type": str(case["case_type"]),
                   "score": case["final_score"]}
        newCases.append(newCase)

    if len(newCases) != 0:
        users[user_id] = {"cases": newCases}

json_str = json.dumps(users, indent=4, ensure_ascii=False)

with open("G:\python\Analysis"+"\\"+"score.json", 'w', encoding='utf-8') as json_file:
    json_file.write(json_str)
