leaderboard_climb=lambda A,K:(lambda S:[len(S)-__import__('bisect').bisect(S,i)+1for i in K])(sorted(set(A)))
