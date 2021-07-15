def best_match(goals1, goals2):
  # scores makes an array of following structure [(Goal difference, Zamalek Goals, index in the arrays), ...]
  scores = [(zip[0] - zip[1], zip[1], idx) for idx, zip in enumerate(zip(goals1, goals2))]
  # Sorts the score array first by Goal difference first and by Zamalek Goals after (reversed) and get's the first element index
  return sorted(scores, key=lambda y: (y[0], -y[1]))[0][2]
