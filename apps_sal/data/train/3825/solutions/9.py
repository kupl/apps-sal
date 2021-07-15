from re import sub, I
filter_words = lambda phrase: sub("(bad|mean|ugly|horrible|hideous)","awesome", phrase, 0, I)
