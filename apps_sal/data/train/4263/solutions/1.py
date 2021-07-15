import re
apparently=lambda Q:re.sub(r'(?<=\band|\bbut)\b(?! apparently\b)',' apparently',Q)
