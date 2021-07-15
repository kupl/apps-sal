from heapq import nlargest

def max_tri_sum(numbers):
    #your code here
#     print(nlargest(3, set(numbers)))
    return sum(nlargest(3, set(numbers)))
