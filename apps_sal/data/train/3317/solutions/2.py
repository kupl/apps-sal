def gr33k_l33t(string):
    doc = {e[0].lower(): e[-1] for e in 'A=α B=β D=δ E=ε I=ι K=κ N=η O=θ P=ρ R=π T=τ U=μ V=υ W=ω X=χ Y=γ'.split()}
    return ''.join((doc.get(e, e) for e in string.lower()))
