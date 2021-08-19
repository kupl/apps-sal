def main():
    (a, b) = map(int, input().split(' '))
    if b == 1:
        print('0')
        return
    k = (a + 1) * a // 2
    z = k * b + a
    z *= b * (b - 1) // 2
    print(z % (10 ** 9 + 7))
    pass


main()
