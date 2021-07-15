def order_type(arr):
    l = [len(str(i))if type(i)==int else len(i)for i in arr]
    return [["Decreasing","Unsorted"][l!=sorted(l)[::-1]],["Increasing","Constant"][len(set(l))<2]][sorted(l)==l]
