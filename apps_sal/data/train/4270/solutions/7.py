def odd_ball(arr):
    index = arr.index('odd')
    number = [x for x in arr if x == index]
    if len(number) > 0:
        return True
    else:
        return False
