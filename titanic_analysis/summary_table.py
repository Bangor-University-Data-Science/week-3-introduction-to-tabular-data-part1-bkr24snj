import pandas as pd
df = pd.read_csv('data/titanic.csv')
def create_summary_table(df):
    """
    Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        pd.DataFrame: A summary DataFrame.
    """
    summary_df = pd.DataFrame({
        'Feature Name': df.columns,
        'Data Type': df.dtypes.values,
        'Number of Unique Values': [df[col].nunique() for col in df.columns],
        'Has Missing Values?': [df[col].isnull().any() for col in df.columns]
        })
    summary_df.columns = [col.strip() for col in summary_df.columns]
    return summary_df


