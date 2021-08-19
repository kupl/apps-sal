def nba_extrap(ppg, mpg):
    puntos_por_minuto = ppg / mpg
    puntos_totales = round(puntos_por_minuto * 48.0, 1)
    return puntos_totales
