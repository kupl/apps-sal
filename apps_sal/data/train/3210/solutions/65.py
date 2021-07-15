def get_strings(city):
    city_list = list(city.lower())
    empty = []
    abet = [chr(i) for i in range(ord('a'), ord('z')+1)]
    res = ''
    for i in range(0, len(city_list)):
        c = 0
        letter = city_list[i]
        for j in range(0, len(city_list)):
            if letter in abet:
                if letter == city_list[j]:
                    c += 1
                    city_list[j] = ''
            else:
                continue
        if letter in abet:
            res += letter+':'+c*'*'+','               
        else: continue
    return res[0:len(res)-1]
