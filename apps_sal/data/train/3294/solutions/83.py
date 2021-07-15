def converter(mpg):
    kml = (mpg*1.609344)/4.54609188
    return float("%.2f" % round(kml,2))
