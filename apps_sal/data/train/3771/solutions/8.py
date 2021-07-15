validate_number=lambda s:['Plenty more fish in the sea','In with a chance'][bool(__import__('re').fullmatch('(0|\+44)7\d{9}',s.replace('-','')))]
