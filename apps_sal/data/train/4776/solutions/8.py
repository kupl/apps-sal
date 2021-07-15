def length_sup_u_k(n, k):
    a=[1,1]
    count = 0
    for i in range(2,n):
        a.append(a[i-a[i-1]]+a[i-a[i-2]])
        if a[i] >= k:
            count +=1
    return count
def comp(n):
    a=[1,1]
    count = 0
    for i in range(2,n):
        a.append(a[i-a[i-1]]+a[i-a[i-2]])
        if a[i] < a[i-1]:
            count +=1
    return count
