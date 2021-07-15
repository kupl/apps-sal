#d = div (x,b)
#m = mod (x,b)
#x = d*b + m = kmb + m
#значит m любое, k любое, им всегда найдётся соответствующее x.
#m может меняться от b-1, k может меняться от 1 до a
#sum (x) = sum(1..b-1) * m * sum (1..a) * k * b + sum (1..b-1)*m
#sum (x) = sum (1..a) sum (1..b-1) просуммировать: kmb + m
#sum (x) = sum (b-1) * m * sum (1..a) просуммировать: bk + 1
#S(b-1) * (b * S(a) + a)

def S (n):
    return n*(n+1)//2
#
string = input ()
string_list = string.split ()
a,b = int (string_list[0]),int (string_list[1])
itog = S(b-1)* (S(a)*b + a)
itog = int (itog % 1000000007)
print (itog)
