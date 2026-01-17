from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

from build_dataset import build_dataset

def main():
    data = build_dataset()

    # Features (X) and label (y)
    X = [
        [
            row["experience_years"],
            row["avg_rating"],
            row["current_workload"],
            row["availability"],
            row["task_priority"],
            row["estimated_hours"],
            row["skill_match_ratio"],
        ]
        for row in data
    ]
    y = [row["success"] for row in data]

    # Split data (keep it reproducible)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    # Train Logistic Regression (baseline ML model)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)

    print("Accuracy:", round(accuracy_score(y_test, y_pred), 3))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, digits=3))

if __name__ == "__main__":
    main()

