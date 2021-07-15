top3 = lambda x,y,z: [d[0] for d in sorted(list(zip(x,y,z)), key=lambda w: -w[1]*w[2])[:3]]
