gcd=lambda a,b:gcd(b,a%b) if b else a
lcm=lambda a,b:a/gcd(a,b)*b
sum_differences_between_products_and_LCMs=lambda p:sum(x*y-(lcm(x,y) if x and y else 0) for x,y in p)

