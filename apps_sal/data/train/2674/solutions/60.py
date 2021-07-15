import re
def two_sort(array):
    print(array)
    min_value=10000
    min_value2=10000
    min_string=" "
    for x in array:
        if len(x)<2:
            y=ord(x[0])
            min_value=y
            min_string=x
        else:
            y=ord(x[0])
            y2=ord(x[1])
            if y<min_value:
                min_value=y
                min_value2=y2
                min_string=x
            elif y==min_value:
                if y2<min_value2:
                    min_value2=y2
                    min_string=x
                else:
                    continue
            else:
                continue
    return "***".join(min_string)
