# cook your dish here
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    #print(n, k, a)
    b = [i for i in a] * k
    #print(k, a, b)
    new = [0 for i in range(n * k)]
    new[0] = b[0]
    for i in range(n * k):
        new[i] = max([new[i - 1] + b[i], b[i]])
    # print(new)
    print(max(new))
