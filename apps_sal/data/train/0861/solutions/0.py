F = [1, 1]


def fibo():
    for i in range(500):
        F.append(F[-2] + F[-1])


def main():
    fibo()
    while True:
        try:
            (A, B) = list(map(int, input().strip().split()[:2]))
            if A == 0 and B == 0:
                break
            print(len([x for x in F if x >= A and x <= B]))
        except:
            break


main()
