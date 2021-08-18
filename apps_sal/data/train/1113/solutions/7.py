n = int(input())
while(n):
    size = int(input())
    a = []
    a = input().split()
    i = 0
    while(i < len(a)):
        a[i] = int(a[i])
        i += 1
    j = max(a)
    freq = []
    freq = (j + 1) * [0]
    k = 0
    while(k < len(a)):
        if(a[k] != 0):
            freq[a[k] - 1] += 1
            k += 1
    count = max(freq)
    key = freq.index(count) + 1
    print(key, count)
    n -= 1
