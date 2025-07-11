import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Users/anshsingh/Downloads/greendestination.csv") 

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

total_employees = len(df)
left_employees = df[df['attrition'] == 'Yes']
attrition_rate = (len(left_employees) / total_employees) * 100

print(f"\n🧮 Total Employees: {total_employees}")
print(f"👋 Employees Left: {len(left_employees)}")
print(f"📉 Attrition Rate: {attrition_rate:.2f}%\n")

numeric_factors = ['age', 'monthlyincome', 'yearsatcompany']

for factor in numeric_factors:
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x='attrition', y=factor)
    plt.title(f"{factor.capitalize()} vs Attrition")
    plt.xlabel("Attrition")
    plt.ylabel(factor.capitalize())
    plt.tight_layout()
    plt.show()


df['attrition_flag'] = df['attrition'].apply(lambda x: 1 if x == 'Yes' else 0)
correlation = df[['age', 'monthlyincome', 'yearsatcompany', 'attrition_flag']].corr()

print("\n📊 Correlation with Attrition:")
print(correlation['attrition_flag'].sort_values(ascending=False))
