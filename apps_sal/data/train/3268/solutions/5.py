import collections
import json
import re


def words_to_object(s):
    if s == '':
        return '[]'
    d = collections.namedtuple('d', 'name ,id')
    words = s.split(' ')
    names = [x for x in words[::2]]
    ids = [x for x in words[1::2]]
    result = ''
    i = 0
    for i in range(0, int(len(words) / 2)):
        a = d(name=names[i], id=ids[i])
        r = json.dumps(a._asdict()).replace('"', "'")
        r = r.replace('"', '').replace("'name':", 'name :').replace("'id':", 'id :')
        r = re.sub('}', '}, ', r, flags=re.UNICODE)
        result += r
    return '[' + result[0:-2] + ']'
