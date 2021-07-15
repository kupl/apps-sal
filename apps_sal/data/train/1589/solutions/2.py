T = int(input())
while T:
    numbers = input().split()
    N = 0
    A = 0
    pos = 0
    for i in range(len(numbers)):
        if int(numbers[i]) > 30:
            N += 1
        if int(numbers[i]) % 2 == 0:
            A += (int(numbers[i]) * (i + 1))
            pos += (i + 1)
    print(N, '%.2f'%(A/pos))
    T -= 1
