def get_chance(n, x, a):
    # Calculate the probabilty that Peter drink just safe drinks
    # First time the prob equals with (n-x) / n
    # After first shot, the prob equal with ((n-1) - x )/ ( n - 1)
    prob = 1
    while a :
        prob *= (n - x) / n
        n -=1 
        a -=1
    return round(prob, 2)

