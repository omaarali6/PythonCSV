import pandas as pd

'Male and female counters initialized'
MaleCount = 0
FemaleCount = 0


'Declaring input and output files'
file_name = "Employees.csv"
file_name_output = "output.csv"

'reading the csv file'
df = pd.read_csv(file_name)

'removing decimel points from the age column'
df['Age'] = (df['Age']).astype(int)

'converting salaries from USD to EGP (I hope by the time you read this the dollar would still be 30EGP hahaha)'
df['Salary(USD)'] = (df['Salary(USD)']*30)

'remove any duplicate rows'
df.drop_duplicates(subset=None, inplace=True)

'extracting the gender coloumn'
x = df['Gender']


'looping on the gender column to extract how many males and females are there '
for i in x:
	if i == "M":
		MaleCount = MaleCount + 1
	if i == "F":
		FemaleCount = FemaleCount + 1


'printing male/female ratio'
print("the relation between the males and females is " + str(MaleCount/FemaleCount))

'printing the madian salaries'
print("Median Salaries is "+ str(df['Salary(USD)'].mean()))

'printing the average age'
print("Average Age is "+ str(df['Age'].mean()))
df.to_csv(file_name_output, index=False)