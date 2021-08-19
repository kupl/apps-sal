T = int(input())
for case in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    time = []
    for i in range(1, 9):
        time.append(a.count(i))
    print(min(time))
