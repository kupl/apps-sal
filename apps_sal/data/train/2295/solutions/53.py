def main():
    sum = 0
    m = 10**9 + 1
    for _ in range(int(input())):
        a, b = map(int, input().split())
        sum += a
        if a > b:
            m = min(m, b)
    print(sum - m if m <= 10**9 else 0)


main()
