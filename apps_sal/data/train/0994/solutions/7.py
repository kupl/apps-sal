from sys import stdin, stdout
import numpy as np


def main():
    for _ in range(int(stdin.readline())):
        N, X = list(map(int, stdin.readline().split()))
        array = np.array(list(map(int, stdin.readline().split()))).reshape(N, 1)
        # matrix = array + array.T
        count = 0
        adsum = 0
        sum = 0
        # print(matrix)
        valid = list([x for x in range(1, N + 1) if (X / x).is_integer()])
        # print(valid)
        for length in valid:
            for j in range(N - length + 1):
                sum = np.sum(array[j:j + length]) * length
                for k in range(N - length + 1):
                    adsum = length * np.sum(array[k:k + length])
                    if sum + adsum == X:
                        count += 1

        print(count)


def __starting_point():
    main()


__starting_point()
