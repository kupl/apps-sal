#let N be a^2
#n + N = M^2 (our answer)
#n + a^2 = m^2
#stuff in slimesquad chat to read from
import math
def solve(n):
    d = math.ceil(math.sqrt(n)) - 1 #find the last biggest root we can use thats not the same number
    #now we need to go backwards because it cant be bigger than root N
    #we need to find a pair of factors for n (which is equal to x*y in discord) that are the same even and odd
    #or else A wouldnt be even
    print(d)
    for a in range(d, 0, -1):#the last argument is to go backwards
    #if we have Found a factor of N that is below the root(N) (finding the closest factors)
    #We go down from Root (N) because the further we go down, the more further apart the factors are
    #and if the difference gets bigger, we will have a bigger square number because the number
    #we need to find is the difference divided by 2
        if (n % a == 0):
        #then find the second factor it could be
        #we can do this easily
            e = (n/a)  - a
            print((a,e))
            if e % 2 == 0:
                p = e / 2
                return p*p
    return -1

