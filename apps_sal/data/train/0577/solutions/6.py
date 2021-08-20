s = input()
n = eval(input())
for i in range(n):
    w = input()
    cnt = 0
    for j in range(len(w)):
        if w[j] in s:
            cnt += 1
    if cnt == len(w):
        print('Yes')
    else:
        print('No')
