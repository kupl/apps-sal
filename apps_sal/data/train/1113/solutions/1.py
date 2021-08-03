import sys


def main():
    s = sys.stdin.readline
    for t in range(int(s())):
        n = int(s())
        A = list(map(int, s().split()))
        save = {}
        for i in A:
            if i in save:
                save[i] += 1
            else:
                save[i] = 1
        g = max(save, key=save.get)
        now = []
        for num in save:
            if save[num] == save[g]:
                now.append(num)
        now = sorted(now)
        print(now[0], save[g])


def __starting_point():
    main()


__starting_point()
