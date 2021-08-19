def find_multiples(integer, limit):
    # Your code here!
    return [x for x in range(integer, limit + 1) if x % integer == 0]
