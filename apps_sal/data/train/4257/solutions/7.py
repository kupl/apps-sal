def calculate_probability(n):
    p=1
    for i in range(n):
        p=p*(365-i)
    return round(1-p/365**n,2)
