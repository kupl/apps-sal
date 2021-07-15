from collections import Counter

# idea: the difference between k*n and (k+1)*n is n
# for them to have the same digits they must have the same digit sum
# so n must have a digit sum of 0 (mod 9) - n must be divisible by 9
def find_lowest_int(k):
    n = 9
    while True:
        if Counter(str(k*n)) == Counter(str((k+1)*n)):
            return n
        n += 9

