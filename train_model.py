import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

def main():
    # 1. Load the labeled data from CSV
    df = pd.read_csv("labeled_combined.csv")
    
    # 2. Data Cleaning: Remove any rows with missing values
    df.dropna(inplace=True)
    
    # 3. Feature selection: choose the relevant columns for training
    features = ['x_head', 'y_head', 'x_foot', 'y_foot', 'x_ball', 'y_ball']
    X = df[features]
    y = df['label']
    
    # 4. Split the dataset into training (80%) and testing (20%) sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 5. Train the model using a RandomForest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # 6. Model Evaluation: Predict the target on the test set
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    # 7. Print evaluation results in a formatted manner
    print("\n===== Model Evaluation =====")
    print(f"Accuracy: {accuracy:.2f}\n")
    print("Classification Report:")
    print("------------------------")
    print(classification_report(y_test, y_pred))
    
if __name__ == '__main__':
    main()
