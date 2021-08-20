d = [sum((int(n) for n in str(i))) for i in xrange(1001)]


def comfortable_numbers(a, b):
    return sum((i - d[i] <= j <= i + d[i] and j - d[j] <= i <= j + d[j] for i in xrange(a, b + 1) for j in xrange(i + 1, b + 1)))
