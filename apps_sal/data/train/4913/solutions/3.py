def mutations(alice1, bob1, ini, take):
    alice, bob, take_up, initial = alice1.copy(), bob1.copy(), take, ini
    def do(initial):
        for _ in range(bob.count(initial)) : bob.remove(initial)
        for _ in range(alice.count(initial)) : alice.remove(initial)
    find_first=lambda word,li:next((i for i,j in enumerate(li)if sum(k!=l for k,l in zip(j, word))==1 and len(set(j))==4),-1)
    alice__, bob__ = find_first(initial, alice), find_first(initial, bob) 
    do(initial)
    if alice__ == -1 and  bob__ == -1 : return -1
    while True:
        alice__, bob__ = find_first(initial, alice), find_first(initial, bob)
        if take_up:  # bob
            if bob__ == -1 : return  0
            initial = bob[bob__]
        else:  # alice
            if alice__ == -1 : return 1
            initial = alice[alice__]
        do(initial)
        take_up ^= 1
