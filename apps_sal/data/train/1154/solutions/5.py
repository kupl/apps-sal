def main():
    N = int(input())
    Numbers = list(map(int, input().split()))
    NumbersG = list(map(int, input().split()))
    n1 = [0 for i in range(1001)]
    for i in NumbersG:
        n1[i] += 1
    for i in Numbers:
        n1[i] -= 1
    for i in range(len(n1)):
        if n1[i] != 0:
            print(i)
            break


def __starting_point():
    main()


__starting_point()
