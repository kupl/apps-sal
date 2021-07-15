def convert(stg):
    alien = str.maketrans("ao", "ou")
    return stg.translate(alien)
