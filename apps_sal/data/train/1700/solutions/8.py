class DynamicConnectivity(object):
# class takes the number of objects n as input, 
# and initializes a data structure with objects numbered from 
# 0 to N-1
    def __init__(self, n):
        self.a = []

# union connects point p with point q
    def union(self, p, q):
        ip = -1
        for k in range(len(self.a)):
            if p in self.a[k]:
                ip = k
                break
        iq = -1
        for k in range(len(self.a)):
            if q in self.a[k]:
                iq = k
                break
        if ip == iq == -1:
            self.a.append({p,q})
        elif ip == -1 and iq != -1:
            self.a[iq].add(p)
        elif iq == -1 and ip != -1:
            self.a[ip].add(q)
        elif ip != -1 and iq != -1 and ip != iq:
            self.a[ip] |= self.a[iq]
            del self.a[iq]

# connected checks if point p is connected to point q and returns a boolean
    def connected(self, p, q):
        ip = -1
        for k in range(len(self.a)):
            if p in self.a[k]:
                ip = k
                break
        return False if ip == -1 else q in self.a[ip]
