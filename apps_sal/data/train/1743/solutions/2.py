# both approaches work because a and m are relatively prime:
# a is a power of 3 while m is a power of 2

# Since a and m are coprime, a^(phi(m)) = 1 (mod m), where phi(m) is the Euler totient function
# if m is a power of 2, phi(m) = m/2
# then, diving the above equation by a we get: a^(-1) = a^(phi(m)-1) (mod m),
# which is our multiplicative inverse
def ModInv(a, m):
    return pow(a, (m>>1)-1, m)

def Ext_Euclid_Alg(a, m):
    old_r, r = a, m
    old_s, s = 1, 0
    
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    
    return old_s if old_s > 0 else old_s + m


def collatz_steps(n, steps):
    # The fraction we get after applying all the steps is of the form
    # (a*x + b)/m, where x is a number such that the later division results in
    # an integer, a = 3^(#'U'), m = 2^(len(steps)) and b[i] = b[i-1] if 'D' else 3*b[i-1] + 2^i
    a, b, m = 1, 0, 1
    for i, s in enumerate(steps):
        m *= 2
        if s == 'U':
            a *= 3
            b = 3*b + 2**i
    
    # a*x + b = 0 (mod m) (=) a*x = -b (mod m) (=) x = a^(-1)*(-b) (mod m)
    # a^(-1) is the modular multiplicative inverse of a mod m: it is the number y such that
    # a*y = 1 (mod m)
    # It will be calculated using the Extend Euclid's Algorithm
    x = (-b * ModInv(a, m)) % m
    # So the number is between n-m and n+m:
    x += m * (n//m)
    # So the number is greater than n:
    return x + m if x < n else x
