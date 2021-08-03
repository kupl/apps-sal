for i in range(int(input())):
    (a, b) = map(int, input().split(' '))
    evenA = a // 2
    evenB = b // 2
    oddA = (a + 1) // 2
    oddB = (b + 1) // 2
    pairs = (evenA * evenB + oddA * oddB)
    print(pairs)
