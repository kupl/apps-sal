def disarium_number(number):
    return ['Not !!', 'Disarium !!'][number in [89, 135, 175, 518, 598, 1306, 1676, 2427, 2646798] or len(str(number)) == 1]
