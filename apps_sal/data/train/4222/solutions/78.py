def get_size(w,h,d):
    array = []
    area = (w * h) * 2 + (w * d) * 2 + (h * d) * 2
    array.append(area)
    volume = w * h * d
    array.append(volume)
    return array
    #your code here

