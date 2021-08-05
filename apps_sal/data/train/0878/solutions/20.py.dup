# cook your dish here
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    curr = 0
    count = 0
    for i in range(n):
        count += (s[i] - curr - 1) // k
        curr = s[i]
    print(count)
