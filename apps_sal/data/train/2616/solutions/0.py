#!/usr/bin/env python3

def __starting_point():
    x, k = map(int, input().strip().split())
    string = input().strip()

    if eval(string) == k:
        print(True)
    else:
        print(False)


__starting_point()
