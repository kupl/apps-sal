def length_sup_u_k(n, k):
    count = 0
    u_ = u(n)
    for i in range(2,n+1):
        if u_[i] >= k:
            count += 1
    return count
    
def comp(n):
    count = 0
    u_ = u(n)
    for i in range(2,n+1):
        if u_[i] < u_[i-1]:
            count += 1
    return count

def u(n):
    u = [0, 1, 1]
    for i in range(3, n+1):
        u.append(u[i - u[i - 1]] + u[i - u[i - 2]])
    return u
    
    #     if n == 1 or n == 2:
    #         return 1
    #     return u(n - u(n-1)) + u(n - u(n-2))

