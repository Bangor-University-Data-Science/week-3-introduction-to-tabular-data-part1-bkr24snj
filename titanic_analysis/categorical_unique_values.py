import pandas as pd
df = pd.read_csv('data/titanic.csv')
categorical_features = df.select_dtypes(include = ['object', 'category','bool']).columns.to_list()
def display_unique_values(df, categorical_features):
    """
    Displays unique values for each categorical feature in the DataFrame.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        categorical_features (list): List of categorical feature names.
    
    Returns:
        dict: A dictionary where keys are feature names and values are the unique values.
    """
    dict = {}
    for col in categorical_features:
        unique_values = df[col].unique()
        dict[col] = unique_values
    return dict
