
for _ in range(int(input())):
    N = int(input())
    array = []
    for i in range(N):
        a = input()
        first = 0
        second = 0
        for j in range(N // 2):
            first += int(a[j])
        for j in range(N // 2, N):
            second += int(a[j])
        array.append([first, second])
    sm1 = 0
    sm2 = 0
    for i in array:
        sm1 += i[0]
        sm2 += i[1]
    diff = abs(sm1 - sm2)
    for i in array:
        diff = min(diff, abs(sm1 - sm2 - i[0] * 2 + i[1] * 2))
    print(diff)
