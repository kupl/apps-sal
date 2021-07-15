n = int(input())
bb = [0] * 1000001
for _ in range(n):
    a, b = list(map(int, input().split()))
    bb[a] = b
a = 0
for i, b in enumerate(bb):
    if b:
        if i>b :
            a = (bb[i - b - 1] + 1)
        else :
            a=1
            
         
    bb[i] = a
print(n - max(bb))

