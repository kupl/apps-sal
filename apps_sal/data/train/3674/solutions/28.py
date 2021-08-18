def add_binary(a, b):
    def translate_bin(dec):
        if dec == 0:
            return "0"
        elif dec == 1:
            return "1"
        else:
            return translate_bin(dec // 2) + str(dec % 2)

    return translate_bin(a + b)
