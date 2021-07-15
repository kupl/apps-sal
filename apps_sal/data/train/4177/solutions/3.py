def men_from_boys(arr):
    evens = {x for x in arr if x%2==0}
    odds = {x for x in arr if x%2==1}
    return sorted(list(evens))+sorted(list(odds), reverse=True)
