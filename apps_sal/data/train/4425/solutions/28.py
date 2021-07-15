def mango(quantity, price):
        special_price_lots = quantity // 3
        full_price_mangoes = quantity - special_price_lots * 3
        return (special_price_lots * 2 + full_price_mangoes) * price
