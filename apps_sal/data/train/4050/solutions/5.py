def acronym_buster(message):
    acronyms = {'KPI' : "key performance indicators", 
                'EOD' : "the end of the day",
                'EOP' : "the end of the day",
                'TBD' : "to be decided",
                'WAH' : "work at home",
                'IAM' : "in a meeting",
                'OOO' : "out of office",
                'NRN' : "no reply necessary",
                'CTA' : "call to action",
                'SWOT' : "strengths, weaknesses, opportunities and threats"}
    phrases = message.split(".")
    word_lists = []
    for phrase in phrases:
        word_lists.append(phrase.split(" "))
    for word_list in word_lists:
        for word in word_list:
            if len(word) >= 3 and word.isupper():
                if word in acronyms.keys():
                    word_list[word_list.index(word)] = acronyms[word]
                else:
                    return "{} is an acronym. I do not like acronyms. Please remove them from your email.".format(word)
    phrases = []
    for word_list in word_lists:
        phrase = " ".join(word_list)
        if len(phrase)>0 and phrase[0].isalpha() and phrase[0].islower():
            phrase = phrase[0].upper() + phrase[1:]
        elif len(phrase)>0 and phrase[0] == " " and phrase[1].islower():
            phrase = phrase[0] + phrase[1].upper() + phrase[2:]
        phrases.append(phrase)
    message = ".".join(phrases)
    return message
