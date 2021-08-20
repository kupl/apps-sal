r = dict(__import__('re').findall('(\\d{3}).*-\\s(.+)', '\n        039 xxx xx xx - Golden Telecom\n        050 xxx xx xx - MTS\n        063 xxx xx xx - Life:)\n        066 xxx xx xx - MTS\n        067 xxx xx xx - Kyivstar\n        068 xxx xx xx - Beeline\n        093 xxx xx xx - Life:)\n        095 xxx xx xx - MTS\n        096 xxx xx xx - Kyivstar\n        097 xxx xx xx - Kyivstar\n        098 xxx xx xx - Kyivstar\n        099 xxx xx xx - MTS\n        '))


def detect_operator(s):
    return r.get(s[1:4], 'no info')
