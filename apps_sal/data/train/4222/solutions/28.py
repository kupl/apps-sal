def get_size(width, length, height):
    surface_area = 2 * (width * height + width * length + height * length)
    volume = length * width * height
    answer = []
    answer.append(surface_area)
    answer.append(volume)
    return answer
