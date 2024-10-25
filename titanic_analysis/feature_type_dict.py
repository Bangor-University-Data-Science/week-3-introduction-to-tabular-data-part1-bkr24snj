import pandas as pd
df = pd.read_csv('data/titanic.csv')
def create_feature_type_dict(df):
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        dict: A dictionary classifying features into numerical and categorical types.
    """
    dict = {
        'numerical': {
            'continuous': [],
            'discrete': [] 
            },
        'categorical': {
            'nominal': [],  
            'ordinal': []  
            }
        }
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns.to_list()
    continuous_cols = [col for col in numerical_cols if df[col].nunique()>20]
    discrete_cols = [col for col in numerical_cols if df[col].nunique()<=20]
    dict['numerical']['continuous'] = continuous_cols
    dict['numerical']['discrete'] = discrete_cols
    
    categorical_cols = df.select_dtypes(include = ['object', 'category', 'bool']).columns.to_list()
    nominal_cols = [col for col in categorical_cols if col in ['Name', 'Sex', 'Embarked']]
    ordinal_cols = [col for col in categorical_cols if col in ['Pclass']]
    dict['categorical']['nominal'] = nominal_cols
    dict['categorical']['ordinal'] = ordinal_cols
        
    return dict

