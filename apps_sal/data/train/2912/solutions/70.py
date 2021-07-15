def find_multiples(integer, limit):
    arr = []
    [ arr.append(integer * i) for i in range(1,int(limit/integer)+1)]
    return arr
