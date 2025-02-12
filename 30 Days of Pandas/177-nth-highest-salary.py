'''
Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.
'''
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    # Create an empty DataFrame
    salary_df = pd.DataFrame(columns=[f'getNthHighestSalary({N})'])
    # Use only unique values and sort them.
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)

    if N <= 0 or N > len(unique_salaries):
        # Initialize DataFrame with None value
        salary_df.loc[0, f'getNthHighestSalary({N})'] = None
    else:
        # Get Nth highest salary and add to DataFrame
        salary_df.loc[0, f'getNthHighestSalary({N})'] = unique_salaries.iloc[N - 1]
    
    return salary_df
