#!/usr/bin/env python

def main():
    N = int(input())
    while True:
        try:
            X = input()
        except:
            break
        H = list(map(int, X.split()))
        C = 0
        while H:
            e = H.pop(0)
            H2, C1, C2 = list(H), e, 0
            for i in range(len(H2)):
                if H2[i] > e - 1:
                    C2 += H2[i] - (e - 1)
                    H2[i] = e - 1
            # print C+C2, H2, C+C1, H
            if C1 <= C2:
                C += C1
            else:
                C += C2
                H = H2
        print(C)


main()
