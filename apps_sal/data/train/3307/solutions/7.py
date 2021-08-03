def fat_fingers(string):

    fat_string = ""
    count = 0

    for i in string:

        if (i == "a") or (i == "A"):
            fat_string += ""
            count += 1
        else:
            if count % 2 == 1 and i.upper() == i:
                fat_string += i.lower()
            elif count % 2 == 1 and i.lower() == i:
                fat_string += i.upper()
            else:
                fat_string += i

    return fat_string
