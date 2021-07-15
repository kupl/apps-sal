def parse_float(string):
    string="".join(string)
    while True:
        try:
            return float(string)
        except ValueError:
            return None
