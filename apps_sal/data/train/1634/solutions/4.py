from math import factorial


def num_multicombinations(n, k):
    """
    Calculates number of muticombinations of size k from a set of
    size n.
    """
    return factorial(n + k - 1) / factorial(k) / factorial(n - 1)


def num_increasing(x):
    """
    Returns the number of increasing numbers with x digits
    We need to put 8 'increases' into x+1 positions.
    e.g. for 2 digit numbers: 
      ||||d|||d| = 58. four increases before first digit: 1+4 = 5
                       three increases before second digit: 5+3 = 8
    This is equivalent to the number of multicombinations of size 8
    from a set of size x + 1.
    """
    return num_multicombinations(x + 1, 8)


def num_decreasing(x):
    """
    Returns the number of decreasing numbers with x digits
    Similar to num_increasing, but we now have 9 'decreases' to fit
    into x+1 positions. We need to subtract 1 because 000...0000 is
    not an x-digit number.
    """
    return num_multicombinations(x + 1, 9) - 1


def num_non_bouncy(x):
    """
    Returns the number of non-bouncy numbers with x digits
    Add the number of x-digit increasing and decreasing numbers, then
    subtract 9 so that we don't count the 9 numbers which are both increasing
    and decreasing (one repeated digit e.g. 11111, 22222, ...).
     """
    return num_increasing(x) + num_decreasing(x) - 9


def total_inc_dec(x):
    if x == 0:
        return 1
    return sum(num_non_bouncy(a) for a in range(1, x + 1)) + 1

    #count = 0
    # for i in xrange(10**x):
    #    s = str(i)
    #    if len(s)==1:
    #        count += 1
    #        continue
    #    elif all(map(lambda x: x[0]==x[1], zip(s, s[1:]))):
    #        count += 1
    #        continue
    #    elif all(map(lambda x: x[0]>=x[1], zip(s, s[1:]))):
    #        if s[-1] == '0':
    #            count += 1
    #        else:
    #            count += 2
    # return count

    # your code here
