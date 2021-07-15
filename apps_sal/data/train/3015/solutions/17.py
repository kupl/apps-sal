def get_issuer(number):
    nums = str(number)
    n = len(nums)
    return ('AMEX'       if n == 15 and nums[:2] in ('34', '37') else
            'Discover'   if n == 16 and nums[:4] == '6011' else
            'Mastercard' if n == 16 and 51 <= int(nums[:2]) <= 55 else
            'VISA'       if n in (13, 16) and nums[0] == '4' else
            'Unknown')
