teams = int(input())
strength = list(map(int, input().split()))
strength.sort()
rev = 0
for i in range(0, teams):
    for j in range(i + 1, teams):
        rev += strength[j] - strength[i]

print(rev)
