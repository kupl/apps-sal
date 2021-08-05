def Cook(S):
    Counter = dict()
    for i in S:
        if i not in Counter.keys():
            Counter[i] = 0
        Counter[i] += 1
    for i in Counter.values():
        if i > 1:
            return "yes"
    return "no"


for T in range(int(input())):
    S = input()
    print(Cook(S))
