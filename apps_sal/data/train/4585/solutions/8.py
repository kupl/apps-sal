def find(a,b,n):
    str_ = str(a) + str(b)
    for i in range(11 + 20):
        str_ += str(int(str_[-2]) + int(str_[-1]))
        
    return int(str_[n])  if n < 33 else int(str_[(n - 13) % 20 + 13])
