def get_size(w, h, d):
    my_list = []
    area = (w * h * 2) + (h * d * 2) + (w * d * 2)
    volume = w * h * d
    my_list.append(area)
    my_list.append(volume)
    return my_list
