# If we write the decision tree for the problem we can see
# that we can traverse upwards from any node simply by
# dividing by two and taking the floor. This would require
# a reversal of the list generated since we're building it
# backwards.
# 
# If we examine the successor function (x -> {2x, 2x + 1})
# we can deduce that the binary representation of any number
# gives us the steps to follow to generate it: if the n-th (LTR)
# bit is set, we use 2x + 1 for the next element, otherwise we
# choose 2x. This allows us to build the sequence in order.

def climb(n):
    res = []
    cur = 1
    mask = 1 << max(0, n.bit_length() - 2)

    while cur <= n:
        res.append(cur)
        cur = 2*cur + (1 if (n & mask) != 0 else 0)
        mask >>= 1

    return res
