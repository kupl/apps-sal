import sys


def main():
    t = int(input())
    for z in range(t):
        movie = int(input())
        leng = []
        rating = []
        opt = []
        leng = list(map(int, input().split()))
        rating = list(map(int, input().split()))

        i = 0
        opt.append(leng[i] * rating[i])

        index = i
        rate = rating[i]
        value = opt[i]

        for i in range(1, movie):
            opt.append(leng[i] * rating[i])

            if opt[i] > value:
                value = opt[i]
                rate = rating[i]
                index = i
            elif opt[i] == value:
                if rating[i] > rate:
                    value = opt[i]
                    rate = rating[i]
                    index = i
        print(index + 1)


main()
