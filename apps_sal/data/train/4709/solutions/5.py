import numpy as np
def sequence(n):
    return ter2dec(dec2bin(n))
    
def dec2bin(n):
    bin = np.array([])
    while n > 0:
        bin = np.append(bin, [n%2])
        n = n//2
    return bin

def ter2dec(ter):
    dec = 0
    for i in range(len(ter)):
        dec += ter[i]*3**i
    return dec

# Induction hypothesis:
# Let S(n) be the sequence of numbers m that don't form arithmetic sequences, such that m < n.
# For a given k, assume that all S(m) is precisely all the numbers m < k without 2's in their ternary form.
# If m has at least one 2 in it's expansion there exist numbers in the sequence with the 2's repalced by 0's and the 2's replaced by 1's.
#     This forms an arithmetic sequence.
# If m has no 2's, consider A and B such that A,B,m is an arithmetic sequence and B is in S(m).
# Comparing the rightmost digits of B and m which are different. A must have a 2 in this position to form an arithmetic sequence.
#     Hence A is not in S(m) and m will be the next number in the sequence.
# 
# Therefore the next number in the sequence has no 2's in it's ternary form.
#
# Base case: S(1) is 0, S(2) is 0,1.
#
# There is a trivial bijection between the nth numbers ternary form and the binary form of n.


