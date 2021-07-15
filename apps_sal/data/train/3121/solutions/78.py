def solve(arr):
    for num in arr:
        if num > 0 and -num not in arr:
            return num
        elif num < 0 and num-(num*2) not in arr:
            return num
