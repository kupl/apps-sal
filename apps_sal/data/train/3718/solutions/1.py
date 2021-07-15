# For Beginners.

# Time: 11724ms
# it's slow because use isinstance
def divisors5(n):
    return len(list([e for e in [x if n % x == 0 else None for x in range(1, n + 1)] if isinstance(e, int)]))


# Time: 7546ms
# it's little fast because just directly check boolean
def divisors4(n):
    return len(list([e for e in [True if n % x == 0 else False for x in range(1, n + 1)] if e]))


# Time: 4731ms
# in python True is evaluate as 1
# so when prime factorization just set True and sum will return count
def divisors3(n):
    return sum([True if n % x == 0 else False for x in range(1, n + 1)])


# Time: 3675ms
# even don't need return true, cause comparison operator will return boolean
def divisors2(n):
    return sum([n % x == 0 for x in range(1, n + 1)])


# same time with above but make short code via lambda expression
divisors = lambda n: sum([n % x == 0 for x in range(1, n + 1)])

