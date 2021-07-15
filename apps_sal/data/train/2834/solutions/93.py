def symmetric_point(p, q):

# the following equality must be satisfied
# q -p = q -p' 

  p_simx = q[0] -p[0]
  p_simy = q[1] -p[1]

  return [q[0] -(-p_simx), q[1] -(-p_simy)]

