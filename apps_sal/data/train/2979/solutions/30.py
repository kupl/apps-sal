def get_age(age):
    return [int(chr) for chr in age if chr.isdigit()][0]
