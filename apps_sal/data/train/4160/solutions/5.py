get_percentage=lambda s,l=1000:"No e-mails sent"*(s<1)or"%d%%"%(100*s//l)*(s<l)or"Daily limit is reached"
