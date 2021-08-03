n, l = map(int, input().split())
s_l = [str(input()) for _ in range(n)]
s_l = sorted(s_l)
print(''.join(s_l))
