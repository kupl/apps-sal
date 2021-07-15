POWER = {
    # left side
    'w': -4, 'p': -3, 'b': -2, 's': -1,
    # right side
    'm': 4, 'q': 3, 'd': 2, 'z': 1 }

def alphabet_war(fight):
    result = sum( POWER.get(c, 0) for c in fight )
    return "Let's fight again!" if not result else \
          ["Left", "Right"][result > 0] + " side wins!"
