import re
replace_dashes_as_one=lambda s:replace_dashes_as_one(re.sub(r'- *-','-',s))if re.search(r'- *-',s)else s
