#!/bin/python3

import math
import os
import random
import re
import sys


def findMaxScore(mod, arr):

    m = 0

    for i in range(0, len(mod) - 7):
        m = max(m, getScore(mod[i:i + 8], arr))

    return m


def getScore(s, arr):

    m = 1

    score = 0

    for i in range(0, 8):

        if(s[i] == 'd'):
            score += 2 * arr[i]
        elif(s[i] == 't'):
            score += 3 * arr[i]
        elif(s[i] == 'D'):
            score += arr[i]
            m *= 2
        elif(s[i] == 'T'):
            score += arr[i]
            m *= 3
        else:
            score += arr[i]

    return m * score


def __starting_point():

    try:
        n = int(input())

        for _ in range(n):

            l = int(input())
            mod = input()
            arr = [int(y) for y in input().split()]
            print(findMaxScore(mod, arr))

    except EOFError:
        x = 2


__starting_point()
