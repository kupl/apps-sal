def is_inertial(arr):
    try: return sorted([z for z in arr if z%2])[0] > sorted([x for x in arr if x%2==0])[:-1][-1] and max(arr)%2==0 and not not ([z for z in arr if z%2]) if arr else False
    except IndexError: return False 

