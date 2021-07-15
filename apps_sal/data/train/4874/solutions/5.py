def travel(r, zipcode):
    return zipcode + ':' + ','.join([' '.join(x.split()[1:]) for x in [x[:-9] for x in r.split(',') if x[-8:] == zipcode]]) + '/' + ','.join([x.split()[0] for x in [x[:-9] for x in r.split(',') if x[-8:] == zipcode]])
