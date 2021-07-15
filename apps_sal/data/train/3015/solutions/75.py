def get_issuer(number):
    card_types = {'AMEX': {'begin': ('34', '37'), 'num_len': '15'},
                  'Discover': {'begin': '6011', 'num_len': '16'},
                  'Mastercard': {'begin': ('51', '52', '53', '54', '55'), 'num_len': '16'},
                  'VISA': {'begin': '4', 'num_len': ('13', '16')}}
    for k, v in card_types.items():
        if str(number).startswith(v['begin']) and str(len(str(number))) in v['num_len']:
            return k
    return 'Unknown'
