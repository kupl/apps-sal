import re
def frogify(s):
    what = s.replace('.','.&').replace('!','!&').replace('?','?&').replace(',','').replace('-','').replace('(','').replace(')','').replace(';','')
    reason = re.sub(' +', ' ', what)
    reason = reason.split("&")
    hi = reason[:-1]
    arr = []
    for i in hi:
        end = i[-1:]
        result = i[:-1].split(" ")
        final = result[::-1]
        final2 = (" ").join(final)
        if final2[len(final2)-1] == " ":
            final2 = final2[:-1]
        if len(final2) > 0 and final2[0] == " ":
            final2 = final2.lstrip()
        arr.append(final2 + end)
    sun = (" ").join(arr)
    return sun
