def get_size(w,h,d):
    x = w * h * d
    y = 2* ((w * h)+(w * d) + (h * d))
    return [y,x]
    #your code here

