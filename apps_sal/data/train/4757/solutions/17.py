'''     ##     ##  #######  # #  ######
        ##     ##  ##   ##  ###    ##
        ##     ##  ##    #  # #    ##
        #########  #######  # #    ##    '''

import sys
import math
# sys.setrecursionlimit(10**6)

def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))

def printspx(*args): return print(*args, end="")
def printsp(*args): return print(*args, end=" ")
def printchk(*args): return print(*args, end=" \ ")

MODPRIME = int(1e9+7); BABYMOD = 998244353;

def __starting_point():
    # sys.stdin = open("input.txt","r")  # <<<  ^o^  Comment this line  ^_^  >>>
    for _testcases_ in range(int(input())):
        n, m, a, b = get_ints()
        if m/a != n/b :
            print("NO")
        else:
            print("YES")
            matr = [[0]*m for x in range(n)]
            fac = math.ceil(m/a)
            for i in range(n):
                for j in range(a):
                    matr[i][(j+(i*a))%m] = 1
            for i in range(n):
                for j in range(m):
                    printspx(matr[i][j])
                print()
                    
            


# #############################################################################
'''
THE LOGIC AND APPROACH IS BY ME @luctivud ( UDIT GUPTA )
SOME PARTS OF THE CODE HAS BEEN TAKEN FROM WEBSITES LIKE::
(I Own the code if no link is provided here or I may have missed mentioning it)
>>> DO NOT PLAGIARISE.
TESTCASES:
'''
__starting_point()
