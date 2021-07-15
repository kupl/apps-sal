def get_size(w,h,d):
    area = (w*d+w*d) + (d*h+d*h) + (w*h+w*h) 
    volume = (w*h*d)
    return [area, volume] 

