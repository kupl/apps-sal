def caffeineBuzz(n):
  return ["mocha_missing!", "Java", "Coffee"][(n%12==0) + (n%3==0)] + "Script"*(n&1==0)
