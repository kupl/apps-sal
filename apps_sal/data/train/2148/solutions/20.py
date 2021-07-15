n = int(input())
ans = []
while n:
    n += -1
    p, q, b = list(map(int, input().split()))
    if p * pow(b, 99, q) % q: ans.append("Infinite")
    else: ans.append("Finite")
for _ in ans: print(_)

