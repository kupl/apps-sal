def string_color(name):
    if len(name) < 2 :
        return None
    else:
        first = hex(sum(ord(char) for char in name) % 256)[-2:]
        second = 1
        for char in name:
            second = second * ord(char)
        second = hex(second % 256)[-2:]
        third = ord(name[0]) - sum(ord(char) for char in name[1:])
        third = hex(abs(third) % 256)[-2:]
        
        return (first + second + third).upper().replace("X", "0")
