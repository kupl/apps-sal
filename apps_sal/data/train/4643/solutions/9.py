def zipvalidate(postcode):
    try:
        int(postcode)
    except ValueError:
        return False
    if len(postcode) != 6:
        return False
    return all([x != postcode[0] for x in ['0', '5', '7', '8', '9']])
