def sort_csv_columns(csv):
    s = ''
    res = sorted(zip(*[x.split(';') for x in csv.split('\n')]), key=lambda x: x[0].lower())
    for i in range(len(res[-1])):
        s += ';'.join(x[i] for x in res) + '\n'
    return s.strip('\n')
