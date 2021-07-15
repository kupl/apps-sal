def zipvalidate(postcode):
    try:
        int(postcode)
        if postcode[0] not in ['0','5','7','8','9'] and len(postcode) == 6:
            return True
    except:
        pass
    return False
