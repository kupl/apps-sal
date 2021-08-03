teams = int(input())
strength = list(map(int, input().split()))
strength.sort()
rev = 0
for i in range(0, teams):
    rev += strength[i] * (i - (teams - 1 - i))

print(rev)
