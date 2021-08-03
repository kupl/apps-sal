T = eval(input())

while (T > 0):
    S = input()
    res = 0
    for i in range(len(S)):
        if (ord(S[i]) <= 57 and ord(S[i]) >= 49):
            res = res + int(S[i])
    print(res)
    T = T - 1
