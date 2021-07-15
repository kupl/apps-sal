def small_enough(a, limit):
    return list(filter(lambda i: i <= limit, a)) == a
