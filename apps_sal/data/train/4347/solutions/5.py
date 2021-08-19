def are_equally_strong(yL, yR, fL, fR):
    return yL + yR == fL + fR and yL in (fL, fR)
