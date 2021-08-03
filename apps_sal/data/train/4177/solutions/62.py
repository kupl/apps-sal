def men_from_boys(arr):
    boysodd = []
    meneven = []
    for number in arr:
        if number % 2 == 0 and number not in meneven:
            meneven.append(number)
        elif number % 2 != 0 and number not in boysodd:
            boysodd.append(number)
    a = sorted(meneven) + sorted(boysodd, reverse=True)
    return a
