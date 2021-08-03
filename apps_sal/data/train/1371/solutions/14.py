test = int(input())

for _ in range(0, test):
    n, k = list(map(int, input().split()))
    lister = list(map(int, input().split()))
    count = 0
    for x in lister:
        num = x + k
        if num % 7 == 0:
            count += 1
    print(count)
