def men_from_boys(arr):
    men_list = sorted((i for i in arr if i % 2 == 0))
    boy_list = sorted((i for i in arr if i % 2 != 0))
    return list(dict.fromkeys(men_list + boy_list[::-1]))
