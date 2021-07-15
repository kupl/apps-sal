predict=lambda cs, ps: {c: round1(sum(p[0][i]*p[1] for p in ps)/sum(p[1] for p in ps)) for i,c in enumerate(cs)}
