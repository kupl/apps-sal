def travel(r, zipcode):
    streets = []
    nums = []
    addresses = r.split(',')
    for address in addresses:
        if ' '.join(address.split()[-2:]) == zipcode:
            streets.append(' '.join(address.split()[1:-2]))
            nums += address.split()[:1]
    return '{}:{}/{}'.format(zipcode, ','.join(streets), ','.join(nums))
