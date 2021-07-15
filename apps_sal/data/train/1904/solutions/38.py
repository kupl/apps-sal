def compare(p1, p2):
    return (p1[0] ** 2 + p1[1] ** 2) - (p2[0] ** 2 + p2[1] ** 2)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(A, l, r):
    pivot = A[l]
    while l < r:
        while l < r and compare(A[r], pivot) >= 0:
            r -= 1
        
        A[l] = A[r]
        while l < r and compare(A[l], pivot) <= 0:
            l += 1
        
        A[r] = A[l]
    
    A[l] = pivot;
    return l
#     pivot = points[high]
    
#     i = low - 1
    
#     for j in range(low, high):
#         if compare(points[j], pivot) < 0:
#             i += 1
#             swap(points, i, j)
#     swap(points, i + 1, high)
#     return i + 1
    
def quick_select(points, k, low, high):
    while low < high:
        pivot = partition(points, low, high)
        if pivot == k:
            break
        elif pivot < k:
            # need more elements from the right
            low = pivot + 1
        else:
            # reduce element from the left
            high = pivot - 1


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        quick_select(points, k, 0, len(points) - 1)
        return points[:k]
