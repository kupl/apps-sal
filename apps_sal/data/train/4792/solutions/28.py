def parse_float(string):
    try:
        if type(string) == list:
            for i in range(len(string)):
                string[i] = float(string[i])
            return string
        return float(string)
    except ValueError:
        return None
