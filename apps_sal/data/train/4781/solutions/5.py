import math


def spider_to_fly(spider, fly):
    angle_default = 45.0
    list_of_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    angle_multiplier = abs(list_of_letters.index(spider[0]) - list_of_letters.index(fly[0]))
    angle = angle_default * angle_multiplier * math.pi / 180
    sp_num = int(spider[1])
    fl_num = int(fly[1])
    answer = math.sqrt(sp_num ** 2 + fl_num ** 2 - sp_num * fl_num * 2 * math.cos(angle))
    return answer
