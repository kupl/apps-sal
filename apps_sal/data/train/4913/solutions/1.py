def mutations(alice, bob, word, first):
    seen = {word}
    mapping = {0:alice, 1:bob}
    prev_state,state = -1, -1

    def foo(word,first):
        nonlocal state, prev_state
        foo.counter += 1

        if foo.counter > 2 and state < 0 or foo.counter > 2 and prev_state < 0:
            return
        
        for a_word in mapping[first]:
            counter = 0
            for i,x in enumerate(a_word):
                if a_word[i] == word[i]:
                    counter += 1

            if counter == 3 and len(set(a_word))==4 and a_word not in seen:
                seen.add(a_word)
                prev_state = state
                state = first
                word = a_word
                break

        if counter==3 or state < 0:
            return foo(word,first^1)

    foo.counter = 0
    foo(word,first)
    return state
