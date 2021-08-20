teams = int(input())
strength = list(map(int, input().split()))
rev = 0
for i in range(0, teams):
    for j in range(i, teams):
        if i == j:
            continue
        elif strength[i] > strength[j]:
            rev += strength[i] - strength[j]
        else:
            rev += strength[j] - strength[i]
print(rev)
