N = int(input())
for i in range(0, N):
    inp = int(input())
    inpu = input()
    input_list = []
    for j in range(0, inp):
        input_list += [inpu[j]]
    li = []
    if input_list[0] == '1':
        li += [0, 1]
    if input_list[inp - 1] == '1':
        li += [inp - 1, inp - 2]
    for k in range(1, inp - 1):
        if input_list[k] == '1':
            li += [k - 1, k, k + 1]
    li = list(set(li))
    t = inp - len(li)
    if t < 0:
        print('0')
    else:
        print(t)
