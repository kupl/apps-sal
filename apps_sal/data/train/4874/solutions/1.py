import re


def travel(r, zipcode):
    res = [(m.group(2), m.group(1)) for m in re.finditer('(\\d+) ([^,]+) ([A-Z][A-Z] \\d{5})', r) if zipcode == m.group(3)]
    return '{}:{}/{}'.format(zipcode, ','.join((a[0] for a in res)), ','.join((a[1] for a in res)))
