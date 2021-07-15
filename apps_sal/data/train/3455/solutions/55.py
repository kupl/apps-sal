def disarium_number(number):
    n_1 = [int(i) for i in str(number)]
    n = [int(i) for i in range(1, len(n_1)+1)]
    strong = sum([n_1[i]**n[i] for i in range(len(n_1))])
    
    if strong == number:
        return "Disarium !!"
    else:
        return "Not !!"
