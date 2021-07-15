import re;toUnderScore=lambda s:re.sub(r"(?<=[^0-9])(\d+)", r"_\1", re.sub(r"(?<=[^_])([A-Z])(?=[a-z]*)", r"_\1", s[0]+s[1:-1].replace("_","")+s[-1])) if s else ""
