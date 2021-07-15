def gr33k_l33t(string):
  greek = {'A':'α','B':'β','D':'δ','E':'ε','I':'ι','K':'κ','N':'η','O':'θ','P':'ρ','R':'π','T':'τ','U':'μ','V':'υ','W':'ω','X':'χ','Y':'γ'}
  return ''.join(greek.get(c.upper(), c.lower()) for c in string)
