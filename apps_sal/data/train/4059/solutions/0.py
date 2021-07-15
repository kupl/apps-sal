def switch_lights(initial_states):
    states = list(initial_states)
    parity = 0
    for i in reversed(range(len(states))):
        parity ^= initial_states[i]
        states[i] ^= parity
    return states
