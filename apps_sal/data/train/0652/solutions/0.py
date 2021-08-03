t = eval(input())
while t:
    t = t - 1
    s1 = input().lower()
    s2 = input().lower()
    res = "equal"
    for i in range(len(s1)):
        if(s1[i] != s2[i]):

            res = "first" if s1[i] < s2[i] else "second"
            break
    print(res)
