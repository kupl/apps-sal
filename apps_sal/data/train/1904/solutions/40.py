\"\"\"
quick select to find k

quick select method
arr, k (kth)
l = -1
r = len(arr)

def square(e):
    return e[0] * e[0] + e[1] * e[1]


def partition(arr, l, r):
    p = r
    firstHigh = l
    for i in range(r):
        if square(arr[i]) < square(arr[p]):
            arr[i], arr[firstHigh] = arr[firstHigh], arr[i]
    arr[firstHigh], arr[p] = arr[p], arr[firsthHigh]
    return firstHigh
            


def getKClosest(arr, k):
    while l + 1 < r:
        v = partition(arr, l, r)
        if v < k:
            l = v
        else:
            r = v

        retrun arr[:k]

\"\"\"
def square(e):
    return e[0] * e[0] + e[1] * e[1]


def partition(arr, l, r):
    p = r
    firstHigh = l
    for i in range(l, r):
        if square(arr[i]) < square(arr[p]):
            arr[i], arr[firstHigh] = arr[firstHigh], arr[i]
            firstHigh += 1
    arr[firstHigh], arr[p] = arr[p], arr[firstHigh]
    return firstHigh
            
class Solution:
    def kClosest(self, arr: List[List[int]], k: int) -> List[List[int]]:
        l = 0
        r = len(arr) - 1
        while l < r:
            v = partition(arr, l, r)
            if v < k:
                l = v + 1
            else:
                r = v - 1

        return arr[:k]
