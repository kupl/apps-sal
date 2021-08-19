# takes interval from integer to limit
# returns all multiples within this range of integer
def find_multiples(integer, limit):
    return [i for i in range(integer, limit + 1) if i % integer == 0]
