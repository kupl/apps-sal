t = int(input())
while(t):
    t -= 1
    s = input()
    l = []
    l1 = []
    lik = 2
    for i in s:
        if(i not in l):
            l.append(i)
    for i in l:
        l1.append(s.count(i))
    if(len(l) < 3):
        lik = 0
    if(lik == 2):
        l1.sort()
        if l1[-2] + l1[-3] != l1[-1]:
            lik = 1
    if(lik == 0 or lik == 2):
        print("Dynamic")
    if(lik == 1):
        print("Not")
