testcases = int(input())

for _ in range(testcases):
    (N, K) = list(map(int, input().split()))
    array = list(map(int, input().split()))

    max = array[0]
    min = array[0]

    for i in array:
        if i > max:
            max = i
        if i < min:
            min = i

    max = max + K
    min = min - K

    print(abs(max - min))
