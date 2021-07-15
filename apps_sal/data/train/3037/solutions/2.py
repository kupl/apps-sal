from collections import Counter

def obtain_max_number(arr):
    count = Counter(arr)
    while any(value > 1 for value in list(count.values())):
        n = next(key for key in count if count[key] > 1)
        count[n] -= 2
        count[n * 2] += 1
    return max(count)




# without import
#
#def obtain_max_number(arr):
#    s = set(arr)
#    while any(arr.count(n) > 1 for n in s):
#        c = next(n for n in s if arr.count(n) > 1)
#        arr.remove(c)
#        arr.remove(c)
#        arr.append(c*2)
#    return max(arr)

