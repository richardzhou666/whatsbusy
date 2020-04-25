import pandas as pd 

df1 = pd.DataFrame({'days': [1,1,2,2,1,3,4],'values': [10,10,5,3,-2,4,20]})

# Part a
out1 = df1.groupby('days')['values'].agg(['mean', 'median', 'max', 'min'])
out1.columns = ['mean_values', 'median_values', 'max_values', 'min_values']

# Part b
df2 = pd.DataFrame({'employee': [1001, 1002, 1004, 1001, 1001, 1002, 1004, 1005, 1005],
    'pos': [2, 2, 2, 2, 2, 2, 2, 2, 2],
    'amount': [125, 542, 2345, 892, 100, 1234, 657, 34, 35]})

# Find difference between max and min
def diff(args):
	return args.max() - args.min()

out2 = df2.groupby('employee').agg({'pos': 'first','amount':diff}).sort_values('amount', ascending = False).iloc[:2, :]
out2.columns = ['pos', 'amount_diff']
print(out2)

