# cook your dish here
t = int(input())
for _ in range(t):
    N = int(input())
    lst = list(map(int, input().split()))
    maxcc = 0
    el = 0
    for j in range(N):
        i = j
        count = 0
        while i < len(lst):
            if i + 1 < N and lst[i] == lst[i + 1]:
                count += 1
                i += 1
            elif i + 2 <= N - 1 and lst[i] == lst[i + 2]:
                count += 1
                i += 2
            else:
                break
        if count > maxcc:
            maxcc = count
    print(maxcc)
