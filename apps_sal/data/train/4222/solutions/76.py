def get_size(w,h,d):
    "Измеряем объем и площадь коробки"
    s_o = []
    s = (w * h * 2) + (h * d * 2) + (d * w * 2)
    o = w * h * d
    s_o.append(s)
    s_o.append(o)
    return s_o
