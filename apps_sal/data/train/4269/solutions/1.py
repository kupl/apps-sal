def convert_my_dollars(usd, currency):
    di={"Armenian Dram":478, "Bangladeshi Taka":1010010, "Croatian Kuna":110, "Czech Koruna":10101, "Dominican Peso":110000, "Egyptian Pound":18, "Guatemalan Quetzal":111, "Haitian Gourde":1000000, "Indian Rupee":63, "Japanese Yen":1101111, "Kenyan Shilling":1100110, "Nicaraguan Cordoba":11111, "Norwegian Krone":1000, "Philippine Piso":110010, "Romanian Leu":100, "Samoan Tala":11, "South Korean Won":10000100011, "Thai Baht":100000, "Uzbekistani Som":10000, "Venezuelan Bolivar":1010, "Vietnamese Dong":101100000101101}
    if currency[0] in ("A","E","I",'O','U'):
        return f'You now have {di[currency]*usd} of {currency}.'
    else:
        return f'You now have {int(str(di[currency]),2)*usd} of {currency}.'
