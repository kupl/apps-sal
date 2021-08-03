
def solve(arr):
    for n in arr:
        if -n not in arr:
            return n
