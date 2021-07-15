a,b,c = map(int, input().split())
n = int(input())
p = list(map(int, input().split()))
sm = 0
for i in range(len(p)):
    if p[i] > b and p[i] < c:
        sm += 1
print(sm)
