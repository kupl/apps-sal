# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = input().split()
    i = 0
    while i != n and arr[i] != '0':
        i += 1
    sum = 0
    for j in range(i,n):
        if arr[j] == '0':
            sum += 1100
        else:
            sum += 100
    print(sum)


