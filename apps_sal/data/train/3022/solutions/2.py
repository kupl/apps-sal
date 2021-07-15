import heapq
def two_highest(list_):
    return heapq.nlargest(2, set(list_)) if type(list_) == list else False
