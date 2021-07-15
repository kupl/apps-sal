import re
from statistics import mean
trump_detector = lambda s:round(mean(map(len,re.findall(r'(a+|e+|i+|o+|u+)',s.lower())))-1,2)
