def sign(x):
    return (x > 0) - (x < 0)

def is_sorted_and_how(arr):
    s = {sign(y - x) for x, y in zip(arr, arr[1:])}
    if len(s) == 1 or len(s) == 2 and 0 in s:
        return "yes, %s" % ["descending", "ascending"][1 in s]  
    return 'no'
