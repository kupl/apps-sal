from string import punctuation


def pseudo_sort(st):
    capital_list = sorted([word.strip(punctuation) for word in st.split() if word[0].isupper()], reverse=True)
    lower_list = sorted([word.strip(punctuation) for word in st.split() if word[0].islower()])
    return " ".join(lower_list + capital_list)
