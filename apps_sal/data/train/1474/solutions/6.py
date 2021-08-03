t = int(input())
for case in range(t):
    n = int(input())
    a = list(map(str, input().split()))
    k = input()
    max = -1
    for i in a:
        if max < i.count(k):
            max = i.count(k)
            num = i
    print(num)
