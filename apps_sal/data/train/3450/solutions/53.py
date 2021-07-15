def array(string):
    length=len(string.replace(" ", "").replace(",", ""))
    if length >2:
        result= " ".join(string.split(",")[1:-1])
        if result != '':
            return result
        else:
            return None

