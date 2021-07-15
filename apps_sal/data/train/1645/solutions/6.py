#explained at: http://www.zrzahid.com/least-number-of-perfect-squares-that-sums-to-n/
def sum_of_squares(n):
    def is_sq(n): return int(n**0.5) * int(n**0.5) == n
    if is_sq(n): return 1
    while n & 3 == 0: n >>= 2
    if n & 7 == 7: return 4
    for i in range(1,int(n**0.5)):
        if is_sq(n-i*i): return 2
    return 3
