A,x = [],1
while len(A) < 300:
    r = (6**x+3*2**x)//4
    if not r%10:
        A.append(r)
    x += 1

def find_mult10_SF(n):
    return A[n-1]
