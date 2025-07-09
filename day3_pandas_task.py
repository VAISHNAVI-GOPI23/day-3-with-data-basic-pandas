import pandas as pd

# Step 1: Create sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 28],
    'Grade': ['A', 'B', 'A', 'C', 'B'],
    'City': ['NY', 'LA', 'Chicago', 'Houston', 'Seattle']
}

# Step 2: Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Step 3: Display entire DataFrame
print("Initial DataFrame:")
print(df)

print("\nNames and Grades:")
print(df[['Name', 'Grade']])

print("\nStudents aged above 30:")
print(df[df['Age'] > 30])

# Step 4: Add Passed column based on Grade
df['Passed'] = df['Grade'].apply(lambda x: 'Yes' if x in ['A', 'B'] else 'No')

print("\nDataFrame with Passed column:")
print(df)

avg_age = df['Age'].mean()
print("\nAverage Age of Students:", avg_age)
