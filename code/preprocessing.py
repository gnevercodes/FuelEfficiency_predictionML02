
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """Load dataset from a CSV file."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Perform basic cleaning like handling missing values."""
    df = df.dropna()
    return df

def split_features_labels(df, target_column):
    """Split the dataframe into features and target labels."""
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return X, y

def scale_features(X_train, X_test):
    """Scale features using StandardScaler."""
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled
