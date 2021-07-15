def get_ages(s, diff):
    older, younger = (s / 2) + (diff / 2), (s / 2) - (diff / 2)  
    if older >= younger >= 0:
        return (older, younger)
