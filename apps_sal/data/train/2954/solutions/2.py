def riders(A):
    Z=[0]
    for x in A:
        if Z[-1]+x<=100:Z[-1]+=x
        else:Z.append(x)
    return len(Z)
