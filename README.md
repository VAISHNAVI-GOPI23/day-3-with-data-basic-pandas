# Day 3 – Python Pandas Basics

## 📌 **Task**
Today’s task was to practice **basic pandas operations**, a fundamental skill for any Data Analyst or Data Scientist.

---

## 📝 **Theory**

**What is pandas?**  
- `pandas` is a powerful Python library for **data manipulation and analysis**.
- It provides two primary data structures:
  - **Series:** 1-dimensional labelled array.
  - **DataFrame:** 2-dimensional labelled data structure (similar to a table in SQL or Excel).

### ✨ **Key Concepts Practiced**

✅ **Creating DataFrames**  
- Converting a Python dictionary into a pandas DataFrame for easy data analysis.

✅ **Selecting Columns**  
- Retrieving specific columns for focused analysis using `df[['col1','col2']]`.

✅ **Filtering Rows**  
- Applying conditional filters to get rows matching criteria (`df[df['Age'] > 30]`).

✅ **Adding Derived Columns**  
- Creating new columns based on existing data using `.apply()` with a lambda function.

✅ **Calculating Statistics**  
- Using built-in methods like `.mean()` for summary statistics.

---

## 💻 **Code**

```python
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
```

### 🎯 Key Learnings
Practiced data loading and transformation.

Understood DataFrame operations for selection, filtering, and feature engineering.

Calculated summary statistics using pandas.

#### 👩‍💻 Author

Vaishnavi Gopi

- [GitHub](https://github.com/VAISHNAVI-GOPI23)
- [LinkedIn](https://www.linkedin.com/in/vaishnavi-gopi23)


