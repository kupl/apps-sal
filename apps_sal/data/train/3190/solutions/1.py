from itertools import count

PRIMES     = ['11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47', '53', '59', '61', '67', '71', '73', '79', '83', '89', '97']
SET_PRIMES = set(PRIMES)
TAILS      = ['00', '01', '25', '76']        # 2 digits numbers that fulfill the condition 11(76)*11(76) = ...(76)

def solve(a,b):
    maxMissingDigits = len(str(b))-4
    matches = 0
    for nd in range(maxMissingDigits+1):
        for p in PRIMES:
            if nd == maxMissingDigits and int(p + '0'*(nd+2)) > b:                # All next generated numbers would be > b, so break
                break
            for t in TAILS:
                digs = count(0)
                while True:
                    d = ("{:0>"+str(nd)+"}").format(next(digs)) if nd else ''     # Digits to insert in the middle of the number
                    val = int(p+d+t)                                              # val = 2 digits prime + missing digits (up to maxMissingDigits) + 2 digits tail
                    if val > b or len(d) > nd: break                              # Generated value is too high or if the digits to insert exceed the current number of digits sought for, break
                    if str(val**2)[:2] in SET_PRIMES and a <= val:
                        matches += 1
                    if not d: break                                               # If no digits to insert, the loop has to be broken manually after its first iteration
    return matches
