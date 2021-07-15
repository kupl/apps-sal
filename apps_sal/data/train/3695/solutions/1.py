import re
repeat_adjacent=lambda s:sum(len(set(i[0]))>1 for i in re.findall(r'((([a-z])\3+){2,})', s))
