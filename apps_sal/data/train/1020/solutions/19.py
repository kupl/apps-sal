for _ in range(int(input())):
    (N, K) = map(int, input().split())
    array = list(map(int, input().split()))
    value = 0
    for i in range(N):
        if i % 2 == 0 and array[i] == 1:
            if value > 0:
                value += 1
            else:
                value -= 1
        elif i % 2 != 0 and array[i] == 1:
            if value > 0:
                value -= 1
            else:
                value += 1
    if abs(value) >= K:
        print(1)
    else:
        print(2)
