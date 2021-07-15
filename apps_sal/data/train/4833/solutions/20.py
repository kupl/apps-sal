import re
replace_exclamation = lambda s: re.sub(r"[aeiouAEIOU]", "!", s)
