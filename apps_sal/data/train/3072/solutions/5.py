is_narcissistic=lambda*a:all(n.isdigit()and int(n)==sum(int(d)**len(n)for d in n)for n in map(str,a))
