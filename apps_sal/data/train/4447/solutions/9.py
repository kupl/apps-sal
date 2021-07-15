def revamp(s):
  wds = sorted(''.join(sorted(c for c in wd)) for wd in s.split())
  return " ".join(sorted(wds, key=lambda w : sum(ord(c) for c in w)))

