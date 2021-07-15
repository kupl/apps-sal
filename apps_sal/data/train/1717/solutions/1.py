import re
from collections import Counter

top_3_words=lambda t:[w for w,c in Counter(re.findall("'*[a-z][a-z']*",t.lower())).most_common(3)]
