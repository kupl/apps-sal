def find_missing_number(n):
    return sum(list(range(1,len(n)+2))) - sum(n)
