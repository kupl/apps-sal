cmp=lambda a,b,f:(a,b)==(0,0) and -1 or a>b and 0 or a<b and 1 or a==b and not f and 1 or 0
def mutations(alice, bob, word, first):
    score = {0:0, 1:0}
    seen = {word}
    mapping = {0:alice, 1:bob}

    def foo(alice,bob,word,first):
        foo.counter += 1

        if foo.counter > 2 and not score[0] and not score[1]:
            return
        
        for a_word in mapping[first]:
            counter = 0
            for i,x in enumerate(a_word):
                if a_word[i] == word[i]:
                    counter += 1

            if counter == 3 and len(set(a_word))==4 and a_word not in seen:
                seen.add(a_word)
                word = a_word
                score[first] += 1
                break

        if counter==3 or not score[first]:
            return foo(alice,bob,word,first^1)

    foo.counter = 0
    foo(alice,bob,word,first)
    return cmp(score[0],score[1],first)
