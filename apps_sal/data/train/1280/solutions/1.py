# cook your dish here
numbers = int(input())
for x in range(numbers):
    st = input().strip()
    l = len(st)
    res = 0
    j = l - 1
    i = 0
    while(i < j):
        if (st[i] != st[j]):
            res += abs(ord(st[i])-ord(st[j]))
        i = i + 1
        j = j - 1
    if res==0:
        print(0)
    else:
        print(res)
