def odd_ball(arr):
    fl = arr.index("odd")
    for i in arr:
        if type(i) is int:
            if i == fl:
                return True
    return False
