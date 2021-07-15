facts = []
last = 1
for i in range(1, 100001):
 last = last * i % 1589540031
 facts.append(last)
for x in range(eval(input())):
 print(facts[eval(input())-1])
