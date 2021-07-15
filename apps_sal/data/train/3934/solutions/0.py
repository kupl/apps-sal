def pattern(n):
  return "\n".join(["".join([str(y) for y in range(n, x, -1)]) for x in range(n)]);
