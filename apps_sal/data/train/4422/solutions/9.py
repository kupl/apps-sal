"""
l = length of string
m = l (if l is odd) or l - 1 (if l is even)
k = length of a cycle to get back to original string
then (2^k) mod m = 1
"""


def multiplicativeOrder(b, m):
    k, r = 1, 1
    while True:
        r = (r * b) % m
        if r == 1:
            return k
        k += 1


def jumbled_string(s, n):
    l = len(s)
    m = l if l & 1 else l - 1
    k = multiplicativeOrder(2, m)
    answer = s
    for i in range(n % k):
        answer = answer[::2] + answer[1::2]
    return answer
