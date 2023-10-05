import pandas as pd

df = pd.read_excel('supermarket_sales.xlsx')


df = df[['Gender', 'Product line', 'Total']]

print(df)#.head()
 



pivot_table = df.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc='sum')
print(pivot_table)

pivot_table.to_excel('test.xlsx', 'Report', startcol=4)