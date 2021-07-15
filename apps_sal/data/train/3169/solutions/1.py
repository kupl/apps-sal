buf = [0,1,1,2,4]
def count_odd_pentaFib(n):
    while len(buf)<=n:
        buf.append(sum(buf[-5:]))
    return len([i for i in set(buf[:n+1]) if i&1])

