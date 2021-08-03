t = int(input())
for i in range(t):
    n, k = input().split()
    k = int(k)
    n = int(n)
    l = [int(x) for x in input().split()]
    for i in range(k - 1):
        l.append(l[i])
    length = len(l)
    # print(length)
    sum = 0
    for i in range(k):
        sum += l[i]
    max = sum
    end = k - 1
    start = 0
    while end != length:
        if sum > max:
            max = sum
        end += 1
        if(end <= length - 1):
            sum += l[end]
        sum -= l[start]
        start += 1
    print(max)
