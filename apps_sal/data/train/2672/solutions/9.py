def color_probability(color, texture):
    return {('smooth', 'red'): '0.33', ('bumpy', 'red'): '0.57', ('smooth', 'yellow'): '0.33', ('bumpy', 'yellow'): '0.28', ('smooth', 'green'): '0.33', ('bumpy', 'green'): '0.14'}[texture, color]
