def make_string(s):
    return "".join(i[0] for i in s.split()) # first split the sentence by spaces and made list.
                                            # And select the first letter of the every word in the list generated.

