import sys
import math


class Test:
    N = 0
    S = []

    def __init__(self):
        tmp = input().split()
        self.N = int(tmp[0])
        self.S = [int(i) for i in input()]


class Input:
    T = 0
    test = []

    def __init__(self):
        self.T = int(input())
        for i in range(0, self.T):
            self.test.append(Test())


letter = []
letter.append([])
letter.append([])
letter[0].append([])
letter[0].append([])
letter[1].append([])
letter[1].append([])
letter[0][0].append([])
letter[0][0].append([])
letter[0][1].append([])
letter[0][1].append([])
letter[1][0].append([])
letter[1][0].append([])
letter[1][1].append([])
letter[1][1].append([])
letter[0][0][0].append('a')
letter[0][0][0].append('b')
letter[0][0][1].append('c')
letter[0][0][1].append('d')
letter[0][1][0].append('e')
letter[0][1][0].append('f')
letter[0][1][1].append('g')
letter[0][1][1].append('h')
letter[1][0][0].append('i')
letter[1][0][0].append('j')
letter[1][0][1].append('k')
letter[1][0][1].append('l')
letter[1][1][0].append('m')
letter[1][1][0].append('n')
letter[1][1][1].append('o')
letter[1][1][1].append('p')


def getletter(i, j, k, l):
    return letter[i][j][k][l]


def test_case(t: Test):
    sum = 0
    i = 0
    string = ''
    while i + 3 < len(t.S):
        string += getletter(t.S[i], t.S[i + 1], t.S[i + 2], t.S[i + 3])
        i += 4
    print(string)


inp = Input()
for test in inp.test:
    test_case(test)
