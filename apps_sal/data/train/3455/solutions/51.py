def disarium_number(n):
    return [ "Not !!","Disarium !!"][sum(int(k)**i for i, k in enumerate(str(n), 1)) == n]
