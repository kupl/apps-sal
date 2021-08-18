test = int(input())

for _ in range(0, test):
    n = int(input())
    lister = set(map(int, input().split()))
    print(len(lister))
