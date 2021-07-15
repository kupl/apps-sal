def main():
    for i in range(int(input())):
        n = int(input())
        numberFound = False
        sevens = 0
        while (sevens <= n):
            if ((n - sevens) % 7 == 0) and (sevens % 4 == 0):
                numberFound = True
                print(n - sevens)
                break;
            sevens += 1
        if not numberFound:
            print(-1)

def __starting_point():
    main()
__starting_point()
