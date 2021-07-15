def find_difference(a, b):
    vol1=1
    vol2=1
    for i in range(len(a)):
        vol1=vol1*a[i]
        vol2=vol2*b[i]
    return max(vol1,vol2)-min(vol1,vol2)
