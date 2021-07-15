def find_multiples(integer, limit):
    return list([x for x in [i if i % integer == 0 else 0 for i in range(1, limit+1)] if x > 0])
    # Your code here!

