def to_leet_speak(str):
    leet_dict = {' ': ' ','A':'@','B':'8','C':'(','D':'D','E':'3','F':'F','G':'6','H':'#','I':'!','J':'J','K':'K','L':'1','M':'M','N':'N','O':'0','P':'P','Q':'Q','R':'R','S':'$','T':'7','U':'U','V':'V','W':'W','X':'X','Y':'Y','Z':'2'}
    leet_list = []
    for i in str:
        if i in leet_dict.keys():
            leet_list.append(leet_dict.get(i))
    return ''.join(leet_list)
