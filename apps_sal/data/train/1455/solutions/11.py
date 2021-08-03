n = eval(input())
a = list(map(int, input().split()))
for i in range(eval(input())):
    l, r = (int(x) for x in input().split())
    b = a[l - 1:r]
    b.sort()
    sum = 0
    for i in range(1, len(b)):
        j = b[i] - b[i - 1]
        sum += pow(j, 2)
    print(sum)
