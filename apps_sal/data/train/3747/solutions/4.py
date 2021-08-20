def ipv4_address(address):
    return bool(__import__('re').match('(([1-9]?\\d|1\\d\\d|2[0-4]\\d|25[0-5])(\\.(?!$)|$)){4}\\Z', address))
