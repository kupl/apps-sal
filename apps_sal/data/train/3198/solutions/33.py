def check_exam(a,b):
    return max(0, sum((a[i]==b[i])*5-1 for i in range(len(a)) if b[i]))
