def min_sum(arr):
    a=sorted(arr)
    return sum(int(a[i])*int(a[len(a)-1-i]) for i in range(len(a)//2))
