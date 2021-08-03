# cook your dish here
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    count = 1
    for i in range(1, n):
        j = i - 1
        a = 0
        while j >= 0 and j >= i - 5:
            if l[j] > l[i]:
                j -= 1
            else:
                a = 1
                break
        if a == 0:
            count += 1
    print(count)
