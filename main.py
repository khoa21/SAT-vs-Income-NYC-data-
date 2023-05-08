
import pandas as pd
import matplotlib.pyplot as plt
# Read in the income data
income_df = pd.read_csv('ACSDP5Y2010.DP03-2023-05-05T103828.csv')
sat_df = pd.read_csv("SAT__College_Board__2010_School_Level_Results.csv")
dbn = sat_df['DBN']

def boro2dbn(dbn):
    if dbn[2] == "K":
        return "Kings County, New York"
    elif dbn[2] == "X":
        return "Bronx County, New York"
    elif dbn[2] == "M":
        return "New York County, New York"
    elif dbn[2] == "Q":
        return "Queens County, New York"
    elif dbn[2] == "R":
        return "Richmond County, New York"
    else:
        return "NaN"

# Read the csv file
income_df = pd.read_csv('ACSDP5Y2010.DP03-2023-05-05T103828.csv')

# Select desired columns
income_df = income_df.loc[:, ['Label (Grouping)', 'INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!Mean household income (dollars)']]
income_df['Label (Grouping)'] = income_df['Label (Grouping)'].shift(1)
# ter desired rows
income_df = income_df[income_df['Label (Grouping)'].isin(['Bronx County, New York', 'Kings County, New York', 'New York County, New York', 'Queens County, New York', 'Richmond County, New York'])]



sat_df['BORO'] = sat_df['DBN'].apply(boro2dbn)
sat_df['Total SAT'] = sat_df['Critical Reading Mean']+ sat_df['Writing Mean'] + sat_df['Mathematics Mean']
import pandas as pd
import matplotlib.pyplot as plt
# Read in the income data
income_df = pd.read_csv("sethtasking.csv")
sat_df = pd.read_csv("SAT__College_Board__2010_School_Level_Results.csv")
dbn = sat_df['DBN']




sat_df['BORO'] = sat_df['DBN'].apply(boro2dbn)
sat_df['Total SAT'] = sat_df['Critical Reading Mean']+ sat_df['Writing Mean'] + sat_df['Mathematics Mean']
sat_df = sat_df.dropna()
grouped = sat_df.groupby('BORO')[['Number of Test Takers', 'Critical Reading Mean', 'Mathematics Mean', 'Writing Mean', 'Total SAT']].mean()
# display the resulting DataFrame
new_income = income_df.rename(columns ={'County': 'BORO'})

def merge_dataframes(grouped, new_income, BORO):
    mergedf = pd.merge(new_income, grouped[[BORO,'INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!Mean household income (dollars)']], on=BORO, how='left')
    return mergedf

merged_df = merge_dataframes(new_income, grouped, 'BORO')
merged_df.to_csv('sock.csv', index=False)


# select the x and y variables for the scatterplot
y = grouped["Total SAT"]
x = new_income["INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!Mean household income (dollars)"]

# create the scatterplot
plt.scatter(x, y)

# set the x and y axis labels
plt.ylabel("SAT Score")
plt.xlabel("Mean Household Income ($)")

# set the title of the plot
plt.title("Income Correlation with SAT Score")

corr_coef= grouped["Total SAT"].corr(new_income["INCOME AND BENEFITS (IN 2010 INFLATION-ADJUSTED DOLLARS)!!Mean household income (dollars)"])


# display the plot
plt.show()

