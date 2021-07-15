def pattern(n):
  return "\n".join(["".join([str(x) for y in range(x)]) for x in range(1, n + 1)])
