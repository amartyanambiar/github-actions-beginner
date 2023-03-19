import pandas as pd

input_csv = pd.read_csv('input.csv')

input_csv['second'] = input_csv['first'] * 2

input_csv.to_csv('out.csv', index=False)
