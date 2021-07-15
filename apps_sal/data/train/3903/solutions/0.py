import re
validate = lambda msg: bool(re.match('^MDZHB \d\d \d\d\d [A-Z]+ \d\d \d\d \d\d \d\d$', msg))
