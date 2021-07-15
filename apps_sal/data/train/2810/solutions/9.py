def solve(arr):
    return list(map(helper, arr))
    
def helper(str):
    count = 0
    i = 0
    for char in str:
        if ord(char) & 31 == i + 1:
            count += 1
        i += 1
    return count
