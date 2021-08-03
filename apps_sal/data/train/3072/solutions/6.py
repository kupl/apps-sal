is_narcissistic = lambda*a: all(str(n).isdigit()for n in a) and all(int(n) == sum(int(d)**len(n)for d in n)for n in map(str, a))
