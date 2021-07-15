clean_string=c=lambda s,o='':c(s[1:],o[:-1]if'#'==s[0]else o+s[0])if s else o
