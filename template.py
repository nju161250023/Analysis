import json

f = open('score.json', encoding='utf-8')

newCases = []
zero = []
template = {}

res = f.read()
data = json.loads(res)

for key in data:
    cases = data[key]['cases']

    for case in cases:
        if case['case_id'] not in newCases:
            newCases.append(case['case_id'])
            zero.append(0)

for i in range(0, len(newCases)):
    template[newCases[i]] = zero[i]

json_str = json.dumps(template, indent=4, ensure_ascii=False)

with open("G:\python\Analysis"+"\\"+"template.json", 'w', encoding='utf-8') as json_file:
    json_file.write(json_str)