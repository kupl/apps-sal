S = list(input().split())
min = S[0]
ml = len(S[0])
ans = []
for i in S:
    if len(i) < ml:
        ml = len(i)
        min = i
for j in range(len(S)):
    print(min, end=" ")
    print(S[j], end=" ")
print(min)
