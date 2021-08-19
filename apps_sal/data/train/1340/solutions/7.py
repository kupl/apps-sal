# cook your dish here
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    sum1, ctr, arr = 0, 0, []
    for i in range(n):
        if lst[i] > 0:
            ctr += 1
    for i in range(n):
        if i < ctr:
            if lst[i] < 0:
                arr.append(i + 1)
            elif lst[i] > 0:
                sum1 += lst[i]
        else:
            if lst[i] > 0:
                arr.append(i + 1)
                sum1 += lst[i]
    print(sum1)
    print(len(arr), " ".join(list(map(str, arr))))
