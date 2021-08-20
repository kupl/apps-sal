def men_from_boys(arr):
    evens = [i for i in arr if i % 2 == 0]
    odds = [i for i in arr if i % 2 != 0]
    a = list(set(evens))
    b = list(set(odds))
    a.sort()
    b.sort(reverse=True)
    return a + b
