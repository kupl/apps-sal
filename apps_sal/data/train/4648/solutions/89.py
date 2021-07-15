def automorphic(n):
    ns = str(n)
    nsq = str(n**2)
    return "Automorphic" if nsq[-len(ns):] == ns else "Not!!"
