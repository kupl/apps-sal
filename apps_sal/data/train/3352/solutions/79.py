def find_longest(arr):
    listofstrings = [str(item) for item in arr]
    longest = max(listofstrings, key=len)
    longestToInt = int(longest)
    return longestToInt
