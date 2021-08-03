def mix_fruit(arr):
    d1 = {x: 5 for x in 'banana, orange, apple, lemon, grapes'.split(', ')}
    d2 = {x: 7 for x in 'avocado, strawberry, mango'.split(', ')}
    res = sum(d1.get(x.lower(), d2.get(x.lower(), 9)) for x in arr)
    return round(res / len(arr))
