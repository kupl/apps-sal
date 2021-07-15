def get_size(w,h,d):
    area_vol = []
    area_vol.append(2*(w*h+h*d+w*d))
    area_vol.append(w * h * d)
    return area_vol
