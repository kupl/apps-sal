def main():
    t = eval(input())
    for i in range(0, t):
        count = 0
        n = eval(input())
        for j in range(1, n + 1):
            if n % j == 0:
                count += 1
        if count % 2 == 0:
            print("NO\n")
        else:
            print("YES\n")


main()
