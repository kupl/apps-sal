def better_than_average(a, b):
    a.append(b)
    avg=sum(a)/len(a)
    if avg < b:
        return True
    else:
        return False
