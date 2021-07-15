def cost_of_carpet(rW, rL, cW, cCost):
    rW, rL = sorted((rW, rL))
    return "error" if cW < rW or 0 in (rL, rW, cW) else round(min([rL] + [rW]*(rL<=cW)) * cW * cCost, 2)
