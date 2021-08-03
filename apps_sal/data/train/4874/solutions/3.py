import re


def travel(r, zipcode):
    addresses = [address for address in r.split(',') if re.match('\d+ .+ {}$'.format(zipcode), address)]

    streets = []
    houses = []
    for address in addresses:
        house, street = re.findall('(\d+) (.+) .* .*', address)[0]
        streets.append(street)
        houses.append(house)

    return zipcode + ':' + ','.join(streets) + '/' + ','.join(houses)
