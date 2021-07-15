import re;find=lambda s:max(re.findall(r"!+\?+",s)+re.findall(r"\?+!+",s),key=lambda x:(len(x),-s.find(x)),default='')
