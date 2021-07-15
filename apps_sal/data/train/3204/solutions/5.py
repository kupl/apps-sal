def Guess_it(n,m):
  # Return a list of lists for all combinations
  # green, red, blue
  mass = {'green': 5, 'red': 4, 'blue': 3}
  # Find all combinations of n balls whose total mass = m
  output = []
  for i in range(0, n+1):
      for j in range(0, n+1):
          for k in range(0, n+1):
              if i+j+k==n and i*5 + j*4 +k*3 == m:
                  output.append([i, j, k])
  return sorted(output) # Return sorted list
