for _ in range(int(input())):
    a = set(input())
    b = set(input())
    print('Yes' if len(a & b) > 0 else 'No')
