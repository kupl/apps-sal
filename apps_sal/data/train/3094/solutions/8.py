def sum_array(arr):
    try: return sum(arr) - max(*arr) - min(*arr)
    except: return 0
