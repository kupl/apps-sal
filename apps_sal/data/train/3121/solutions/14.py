def solve(lst):
    for num in lst:
        if -num not in lst:
            return num
