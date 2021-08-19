def mygcd(x, y):
    if x % y == 0:
        return y
    else:
        return mygcd(y, x % y)

# reference: http://en.wikipedia.org/wiki/Euclidean_algorithm
# Please note that it does not matter if y is larger than x, because x%y will have value x
# which is passed to variable y in the next iteration. So the number of iterations is only
# increased by one, but the solution will still be correct.
