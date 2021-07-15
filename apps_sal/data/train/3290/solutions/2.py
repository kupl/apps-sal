def get_ages(s, diff):
    older = (s / 2) + (diff / 2)
    younger = (s / 2) - (diff / 2)
    
    if older >= younger >= 0:
        return (older, younger)
