def zipvalidate(postcode): return bool(__import__('re').match(r'^[12346]\d{5}\Z', postcode))
