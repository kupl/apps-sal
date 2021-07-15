from math import floor
def balanced_num(number):
    summ_1 = 0
    summ_2 = 0
    center = 0
    value = len(str(number))
    if value < 3:
        return "Balanced"
    if value % 2 == 0:
        center = int(len(str(number))/2)
        center_2 = int((len(str(number))/2)-1)
        for i in range(center_2):
            if i != center or i != center_2:
                summ_1 += int(str(number)[i])
                summ_2 += int(str(number)[len(str(number))-i-1])

    else:
        center = floor(len(str(number))/2)
        for j in range(center):
            if j != int(center):
                summ_1 += int(str(number)[j])
                summ_2 += int(str(number)[len(str(number))-j-1])
    if summ_1 == summ_2:
        return "Balanced"
    else:
        return "Not Balanced"
