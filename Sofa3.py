import pandas as pd

df = pd.read_csv('bike.csv', index_col=0) 

average_sales = df.mean(axis=0)

average_df = pd.DataFrame(average_sales, columns=['Average Sales'])

average_df.to_csv('average.csv')

print("Average sales have been calculated and saved to 'average.csv'.")
