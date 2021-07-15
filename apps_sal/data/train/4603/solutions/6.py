def deepAck(m,n):
    return n+1 if m == 0 else deepAck(m-1,1) if n == 0 else deepAck(m-1, deepAck(m,n-1))

def Ackermann(m,n):
    return None if not isinstance(m, int) or not isinstance(n, int) or m < 0 or n < 0 else deepAck(m,n)
