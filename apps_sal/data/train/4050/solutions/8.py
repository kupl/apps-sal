import re


def acronym_buster(message):
    new_msg = message
    subs = {'KPI': "key performance indicators",
            'EOD': "the end of the day",
            'TBD': "to be decided",
            'WAH': "work at home",
            'IAM': "in a meeting",
            'OOO': "out of office",
            'NRN': "no reply necessary",
            'CTA': "call to action",
            'SWOT': "strengths, weaknesses, opportunities and threats"}
    for item in re.findall('(?:\w)*[A-Z]{3,}(?:\w)*', new_msg):
        if item in subs:
            new_msg = new_msg.replace(item, subs[item])
        elif item.isupper():
            return '{} is an acronym. I do not like acronyms. Please remove them from your email.'.format(item)
    # Now capitalize the first "word" in each sentence
    sentences = new_msg.split('. ')
    return '. '.join(s[:1].upper() + s[1:] for s in sentences)
