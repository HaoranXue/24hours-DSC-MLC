import pandas
df = pandas.DataFrame([{'c1':3,'c2':10},{'c1':2, 'c2':30},{'c1':1,'c2':20},{'c1':2,'c2':15},{'c1':2,'c2':100}])
df = df.sort_values(by='c1', ascending=[True])
print(df)