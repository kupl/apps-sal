# cook your dish here
for h in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    c = n
    for i in range(n):
        j = i - 1
        while j >= i - 5 and j >= 0:
            if l[i] >= l[j]:
                c -= 1
                break
            j -= 1
    print(c)
