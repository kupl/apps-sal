def calculate_total(t1, t2):
    t1s=sum(t1) if t1 else -1
    t2s=sum(t2) if t2 else -1
    return True if t1s > t2s else False
