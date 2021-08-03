for _ in range(int(input())):
    a = int(input())
    b = int(input())
    c = int(input())
    if a == 1 or b == 1 or c == 1:
        print(0)
    else:
        print(4 * (a + b + c - 6))
