from functools import reduce; gcd=lambda a,b: gcd(b,a%b) if b else a; final_attack_value=lambda x,m: reduce(lambda a,b: a+b if a>=b else a+gcd(a,b),m,x)
