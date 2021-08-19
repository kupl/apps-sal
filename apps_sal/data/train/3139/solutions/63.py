def index(array, n):
    if n < len(array):
        target = array[n]
        ans = target ** n
        return ans
    else:
        return -1
