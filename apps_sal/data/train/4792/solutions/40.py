def parse_float(string):
    x = [string]
    for item in x:
        try:
            return float(item)
        except:
            return
