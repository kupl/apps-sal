import re
count_robots = lambda a, b='[|};&#\[\]/><()*]{2}', l='[a-zA-Z]': ['%d robots %s %s' %
                                                                  (sum(len(re.findall(l + b + '0' + b + '0' + b + l, s)) * (r in s.lower())for s in a), m, r)
                                                                  for m, r in [("functioning", "automatik"), ("dancing", "mechanik")]]
