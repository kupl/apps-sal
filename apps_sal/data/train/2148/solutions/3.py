print('\n'.join([(lambda p, q, b: 'Infinite' if p * pow(b, 99, q) % q else 'Finite')(*list(map(int, input().split()))) for _ in range(int(input()))]))
