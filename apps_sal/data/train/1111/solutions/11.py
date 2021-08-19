# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    but = list(map(int, input().split()))
    odd = [i % 2 for i in but]
    no = odd.count(1)
    ne = odd.count(0)
    ans = no * ne
    print(ans)
