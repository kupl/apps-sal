a = int(input())
q = list(map(int, input().split()))
n = int(input())
cost = list(map(int, input().split()))
t = min(q)
cost.sort()
total = 0
index = len(cost) - 1
while(index >= 0):
    r = t
    if(index >= t):
        r = t
        while(r):
            total += cost[index]
            r -= 1
            index -= 1
        if(index >= 2):
            index -= 2
        else:
            break
    else:
        total += sum(cost[0:index + 1])
        break
print(total)
