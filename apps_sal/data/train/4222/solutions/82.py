
def get_size(w,h,l):
    surface_area=2*(h*w)+2*(h*l)+2*(w*l)
    volume=h*w*l
    return [surface_area,volume]
