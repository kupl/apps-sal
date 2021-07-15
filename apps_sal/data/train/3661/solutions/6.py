def find_part_max_prod(n):
    if(n==2):
        return [[1, 1], 1]
    if(n==3):
        return [[2, 1], 1]
    if(n%3==0):
        return [[3]*(n//3), pow(3, n//3)]
    if(n%3==2):
        return  [[3]*((n-2)//3) + [2] , 2 * pow(3, (n-2)//3)]
    if(n%3==1):
        return [[4] + [3]*((n-4)//3), [3]*((n-4)//3) + [2, 2], 4 * pow(3, (n-4)//3)]
