T = int(input())
for ca in range(0, T):
    (x, y) = input().split(' ')
    z = int(str(int(x[::-1]) + int(y[::-1]))[::-1])
    print(z)
