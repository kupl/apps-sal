def commas(num):
    return "{:,.3f}".format(num).rstrip("0").rstrip(".")
