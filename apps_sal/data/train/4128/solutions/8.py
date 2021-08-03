bears = lambda x, s, k='', i=0: [k, len(k) >= x * 2]if i == len(s)else bears(x, s, k + s[i:i + 2], i + 2)if s[i:i + 2] in ['8B', 'B8']else bears(x, s, k, i + 1)
