# ******************************************************************************
# Problem: Fierce Battles
# Link: http://www.codechef.com/OCT12/problems/DRGNBOOL
# Author: Deepak Antony - "deebee" "drunkbeast" "dAbeAst"
# Solution: simple; sum up the total for each level and subtract from the 
# sofloats total capacity for that level; in the end sum up all levels with
# positive diff's
# ******************************************************************************

# Uncomment this line if the judge supports psyco
# import psyco
# psyco.full()

import time
import sys

def timeElapsed(fn):
    """ A time elapsed decorator """
    def wrapper(*args, **kwargs):
        start = time.time()
        res = fn(*args, **kwargs)
        sys.stderr.write("Time Elapsed: %f seconds\n"%(time.time()-start))
        return res
    return wrapper

def solveFierceBattles():
    T = int(input())
    for test in range(T):
        N, M = tuple( int(x) for x in input().split() )
        soints = {}
        for ints in range(N):
            chakra, level = tuple( int(x) for x in input().split() )
            if level not in soints:
                soints[level] = chakra
            else:
                soints[level] += chakra
        sofloats = {}
        for floats in range(M):
            chakra, level = tuple( int(x) for x in input().split() )
            if level not in sofloats:
                sofloats[level] = chakra
            else:
                sofloats[level] += chakra
        res = 0
        for level, chakra in soints.items():

            if chakra < sofloats[level]:
                res += sofloats[level]-chakra
        print(res)
        

@timeElapsed
def main():
    """ Main controller """
    # solve a problem here
    solveFierceBattles()

def __starting_point():
    main()

__starting_point()
