import pandas as pd


def top3(products, amounts, prices):
    df = pd.DataFrame({
        'Product': products,
        'Amount': amounts,
        'Price': prices})
    df['Revenue'] = df['Amount'] * df['Price']
    df.sort_values(by=['Revenue'], ascending=False, inplace=True)
    product_sort = df['Product'].values.tolist()
    return product_sort[0:3]
