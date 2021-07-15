def climb(n):
    #your code here
    return  [n>>n.bit_length()-i-1 for i in range(n.bit_length())]

