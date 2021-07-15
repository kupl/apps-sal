def best_match(goals1, goals2):
  bestDiff = goals1[0] - goals2[0]
  bestIndex = 0
  for i in range(len(goals1)):
      if goals1[i] - goals2[i] < bestDiff:
          bestIndex = i
          bestDiff = goals1[i] - goals2[i]
      if (goals1[i] - goals2[i] == bestDiff) and (goals2[i] > goals2[bestIndex]):
          bestIndex = i
          bestDiff = goals1[i] - goals2[i]
  return bestIndex
