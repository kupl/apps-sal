for _ in range(int(input())):
    X, Y, K = map(int, input().split())
    print('Paja' if ((X + Y) // K) % 2 else 'Chef')
