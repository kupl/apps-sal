def main():
    for _ in range(int(input())):
        (a, b) = list(map(int, input().split()))
        while not (a == 1 and b == 1):
            if a == b or a == 0 or b == 0:
                break
            if a == max(a, b):
                a = a % b
            else:
                b = b % a
        if a == 1 and b == 0 or (a == 0 and b == 1):
            print('YES')
        else:
            print('NO')


main()
