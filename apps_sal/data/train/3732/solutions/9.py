def is_madhav_array(arr):
    (r, x, c) = ([], 1, len(arr))
    try:
        while arr:
            t = 0
            for i in range(x):
                t += arr.pop(0)
            r.append(t)
            x += 1
        return len(set(r)) == 1 and c > 1
    except:
        return False
