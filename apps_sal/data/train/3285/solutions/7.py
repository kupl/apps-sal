import re;trump_detector=lambda trump_speech:(lambda lst:round(sum(lst)/len(lst),2))([len(t[1])for t in re.findall(r'([aeiou])(\1*)',trump_speech,re.I)])
