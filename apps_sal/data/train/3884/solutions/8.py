import re
changes = {'probably':'prolly','Probably':'Prolly','i am':'i\'m','I am':'I\'m','instagram':'insta',
           'Instagram':'Insta','do not':'don\'t','Do not':'Don\'t','going to':'gonna','Going to':'Gonna',
           'combination':'combo','Combination':'Combo'}


def gym_slang(phrase):
    for k in changes.keys():
        if k in phrase:
            phrase = re.sub(k,changes[k],phrase)
    return phrase
