def order_weight(string):
    strng = string.split()
    for i in range(0, len(strng)):
        for j in range(0, len(strng)):
            if (weight(strng[i]) < weight(strng[j])):
                pass
            elif (weight(strng[i]) == weight(strng[j])):
                if(strng[i] <= strng[j]):
                    pass
                else:
                    print(strng[i], strng[j])
                    strng[i], strng[j] = strng[j], strng[i]
            else:
                print(strng[i], strng[j])
                strng[i], strng[j] = strng[j], strng[i]
    strng.reverse()
    final = " ".join(strng)
    return final


def weight(st):
    weight = 0
    for i in range(len(st)):
        weight = weight + int(st[i])
    return weight
