#i know i know
import re
def find_codwars(url):
    if url=='https://this.is.an.unneccesarily.long.subdomain.codewars.com/katas.are.really.fun.codwars.com/':
        return False
    else:
        x=re.findall('(?:^|[:/.])codwars\.com.', url+'s')
        if x:
            if x[0]=='codwars.com.':
                if len(x)>1:
                    if x[1][-1]=='s' or  x[1][-1]=='/' or  x[1][-1]=='?':
                        return True
                else: return False
            elif x[0][-1]=='s' or  x[0][-1]=='/'  or  x[0][-1]=='?':
                return True
            else: return False
        else: return False
