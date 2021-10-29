import random
import json

with open("people.json", "r") as f:
    people = json.load(f)

def make(people):
    pre = [i for i in range(len(people))]
    post = [i for i in range(len(people))]

    result = {}
    pairing = True
    while pairing:
        choice = random.choice(people)
        index = random.randint(0, len(people) - 1)
        if choice not in pre:
            pre[index] = choice
        if choice not in post:
            post[index - 1] = choice
        total = 0
        for i in people:
            if i in pre and i in post:
                total += 1
        if total >= len(people):
            for i in range(len(people)):
                result[pre[i]] = post[i]
            pairing = False
    return result

result = make(people)

with open("previous.json", "r") as f:
    previous = json.load(f)

with open("previous.json", "w") as f:
    for person in result:
        previous[person] = result[person]
    f.write(json.dumps(previous))

with open("list.txt", "w") as f:
    doc = ""
    for i in result:
        doc += f"{i} --> {result[i]}\n"
    f.write(doc)