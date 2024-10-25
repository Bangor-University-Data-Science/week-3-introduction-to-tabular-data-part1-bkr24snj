import pandas as pd
import numpy as np
df = pd.read_csv('data/titanic.csv')
numerical_features = df.select_dtypes(include=[np.number]).columns.tolist()
def get_numerical_df(df, numerical_features):
    """
    Creates a DataFrame containing only numerical features.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        numerical_features (list): List of numerical feature names.
    
    Returns:
        pd.DataFrame: DataFrame containing only numerical features.
    """
    numerical_df = df[numerical_features].select_dtypes(include=[np.number])
    return numerical_df

