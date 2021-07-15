arr = []
n = int(input())
for T in range(n):
    s = list(input().split())
    arr.append(s)
arr.reverse()
for i in arr:
    i.reverse()
    for j in i:
        if j.isalpha():
            print(j,end=' ')
        else:
            print(j[:len(j)-1],end=' ')
    print()

