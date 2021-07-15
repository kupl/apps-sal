def encode(n,strng):
    new_strng = strng.split(" ")
    for i in range(n):
        strng = "".join(strng.split(" "))
        strng = strng[-n:] + strng[:-n]
        index_0 = 0
        for i in range(len(new_strng)):
            index = len(new_strng[i]) + index_0
            new_strng[i] = strng[index_0:index]
            index_0 = index
        strng = ""
        for i in new_strng:
            change = n % len(i) if len(i) != 0 else i.count(" ")
            strng += i[-change:] + i[:-change] + " "
        strng = strng[:-1]
    return f"{n} " + strng

def decode(strng):
    i = 0
    num = ""
    while strng[i].isdigit():
        num += strng[i]
        i += 1
    num = int("".join(num))
    strng = strng[len(str(num))+1:]
    new_strng = strng.split(" ")
    strng = "".join(strng.split(" "))
    for i in range(num):
        index_0 = 0
        for i in range(len(new_strng)):
            index = len(new_strng[i]) + index_0
            new_strng[i] = strng[index_0:index]
            index_0 = index
        strng = ""
        for i in new_strng:
            change = num % len(i) if len(i) != 0 else i.count(" ")
            strng += i[change:] + i[:change]
        strng = strng[num:] + strng[:num]
    index_0 = 0
    for i in range(len(new_strng)):
        index = len(new_strng[i]) + index_0
        new_strng[i] = strng[index_0:index]
        index_0 = index
    return " ".join(new_strng)
