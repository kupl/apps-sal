import re


def travel(r, zipcode):
    r = r.split(',')
    filtered = [*filter(lambda x: re.search(f'{zipcode}$', x), r)]
    (nums, streets) = ([], [])
    for address in filtered:
        (num, street) = address.split(' ', 1)
        nums.append(num)
        streets.append(street.rstrip(' ' + zipcode))
    return filtered != [] and zipcode and f"{zipcode}:{','.join(streets)}/{','.join(nums)}" or f'{zipcode}:/'
