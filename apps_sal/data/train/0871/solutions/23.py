# Contest Code: PRACTICE      Problem Code: ANTEATER
#
# Author: Keyur Shroff
# Date: 24 June 2019

import math
from collections import defaultdict

# --- Function to calculate nCr
def nCr(n,r):
    f = math.factorial
    return (f(n) // f(r)) // f(n-r)

# --- Main Program ---
def main() :
    t = int(input())
    for _ in range(t) :
        r, c = map(int, input().split())
        matrix = []
        for i in range(r) :
            data = list(input())
            matrix.append(data)
        
        timeHorizon = defaultdict(int)
        for i in range(r) :
            for j in range(c) :
                if (matrix[i][j] == "U") :
                    step = 1
                    for k in range(i-1, -1, -1) :
                        if (matrix[k][j] == "#") :
                            break
                        timeHorizon[(step,k,j)] += 1
                        step += 1
                elif (matrix[i][j] == "D") :
                    step = 1
                    for k in range(i+1, r, 1) :
                        if (matrix[k][j] == "#") :
                            break
                        timeHorizon[(step,k,j)] += 1
                        step += 1
                elif (matrix[i][j] == "L") :
                    step = 1
                    for k in range(j-1, -1, -1) :
                        if (matrix[i][k] == "#") :
                            break
                        timeHorizon[(step,i,k)] += 1
                        step += 1
                elif (matrix[i][j] == "R") :
                    step = 1
                    for k in range(j+1, c, 1) :
                        if (matrix[i][k] == "#") :
                            break
                        timeHorizon[(step,i,k)] += 1
                        step += 1
        
        # Count total number of pairs of ants that meet each other
        count = 0
        for key in timeHorizon :
            if (timeHorizon[key] > 1) :
                ants = timeHorizon[key]
                count += nCr(ants, 2)
        
        print(count)


def __starting_point():
    #import profile
    #profile.run('main()')
    main()
    
__starting_point()
