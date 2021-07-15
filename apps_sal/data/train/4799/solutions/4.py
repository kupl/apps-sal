from fractions import Fraction
import math

def comb(m,n):
    return math.factorial(m)//(math.factorial(n)*math.factorial(m-n))

def simplify(a,b):
    return [a // math.gcd(a, b), b // math.gcd(a, b)]

arr=[[1,1],[-1,2]]

def _b(n):
    product_denominators=1
    triangles = []
    for i in range(0,n):
        p=comb(n,i)
        triangles.append(p)
        if i<len(arr):
            product_denominators*=arr[i][1]
    sum_numerator=0
    for i in range(0,n-1):
        p = (product_denominators * arr[i][0] // arr[i][1]) * triangles[i]
        sum_numerator += p
    [a, b] = simplify(-sum_numerator, product_denominators * triangles[-1])
    arr.append([a,b])
def b(n):
    if n%2 and n>1:
        return 0
    if n>=len(arr):
        for i in range(len(arr)+1,n+2):
            _b(i)
    return arr[n]


def series(k, nb) :
    if k>0 and k%2==0:
        temp = b(k)
        bk = abs(temp[0] / temp[1])
        fk = math.factorial(k)
        return (1 / 2) * bk * (2 * math.pi) ** k / fk
    elif k>0 and k%2:
        sum=0
        for i in range(1,nb):
            sum+=1/(i)**k
        return sum
    elif k<0:
        temp = b(1 - k)
        bk = temp[0] / temp[1] if type(temp) is list else temp
        return (-1) ** (-k) * bk / (1 - k)
