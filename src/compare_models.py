from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

from build_dataset import build_dataset

def evaluate(model, X_test, y_test):
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_test, y_pred, average="binary", zero_division=0
    )
    return acc, precision, recall, f1

def main():
    data = build_dataset()

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

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Random Forest": RandomForestClassifier(
            n_estimators=200, random_state=42, class_weight="balanced"
        ),
    }

    print("Model Comparison (test set)")
    print("-" * 60)
    print(f"{'Model':25s}  Acc   Prec  Recall   F1")
    print("-" * 60)

    for name, model in models.items():
        model.fit(X_train, y_train)
        acc, prec, rec, f1 = evaluate(model, X_test, y_test)
        print(f"{name:25s}  {acc:.3f}  {prec:.3f}  {rec:.3f}  {f1:.3f}")

if __name__ == "__main__":
    main()

