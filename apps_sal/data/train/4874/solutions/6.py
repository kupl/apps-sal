def travel(r, zipcode):
    matches = [' '.join(i.split()[:-2]) for i in r.split(',') if ' '.join(i.split()[-2:]) == zipcode]
    return '%s:' % zipcode + ','.join([' '.join(i.split()[1:]) for i in matches]) + '/' + ','.join([''.join(i.split()[:1]) for i in matches])
