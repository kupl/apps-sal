def zipvalidate(postcode):
    return bool(__import__('re').match('^[12346]\\d{5}\\Z', postcode))
