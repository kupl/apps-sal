n = int(input())
branches = list(map(int, input().split()))
for i in range(int(input())):
    (branch, parrot) = list(map(int, input().split()))
    if branch > 1:
        branches[branch - 2] = branches[branch - 2] + parrot - 1
    if branch < n:
        branches[branch] = branches[branch] + branches[branch - 1] - parrot
    branches[branch - 1] = 0
for i in branches:
    print(i)
