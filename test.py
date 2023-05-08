# create an example DataFrame
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                   'Age': [25, 30, 35],
                   'Gender': ['Female', 'Male', 'Male']})

# create a new DataFrame with specific columns and rows
new_df = df.loc[df['Age'] > 28, ['Name', 'Gender']]

# display the new DataFrame
print(new_df)
