# cook your dish h
for _ in range(int(input())):
    a = list(input())
    
    len_a = len(a)
    i = 0
    for i in range(i+1, len_a):
        if(a[i-1] == '0' and a[i] == '1'):
            a = a[:i]
            break
    if('1' in a):
        print(a.count('0'))
    else:
        print(0)

