import csv
from pathlib import Path
from recommend import recommend_employees
from baseline import baseline_recommend

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

def load_employees(path):
    employees = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            employees.append({
                "employee_id": row["employee_id"],
                "name": row["name"],
                "skills": [s.strip() for s in row["skills"].split(",")],
                "experience_years": float(row["experience_years"]),
                "avg_rating": float(row["avg_rating"]),
                "current_workload": float(row["current_workload"]),
                "availability": int(row["availability"]),
            })
    return employees

def load_tasks(path):
    tasks = {}
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tasks[row["task_id"]] = {
                "task_id": row["task_id"],
                "title": row["title"],
                "category": row["category"],
                "required_skills": [s.strip() for s in row["required_skills"].split(",")],
                "priority": int(row["priority"]),
                "estimated_hours": float(row["estimated_hours"]),
            }
    return tasks

def load_relevance(assignments_path):
    """
    Ground truth:
    success = 1 => relevant employee for that task
    """
    relevant = {}
    with open(assignments_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row["success"]) == 1:
                relevant.setdefault(row["task_id"], set()).add(row["employee_id"])
    return relevant

def precision_recall_at_k(recommended_ids, relevant_ids, k):
    if not relevant_ids:
        return 0.0, 0.0
    hits = sum(1 for e in recommended_ids[:k] if e in relevant_ids)
    precision = hits / k
    recall = hits / len(relevant_ids)
    return precision, recall

def evaluate(method_name, recommender_fn, tasks, employees, relevant_map, k=3):
    precisions, recalls = [], []
    for task_id, task in tasks.items():
        relevant = relevant_map.get(task_id, set())
        if not relevant:
            continue
        recs = recommender_fn(task, employees, top_k=k)
        rec_ids = [r["employee_id"] for r in recs]
        p, r = precision_recall_at_k(rec_ids, relevant, k)
        precisions.append(p)
        recalls.append(r)

    avg_p = sum(precisions) / len(precisions)
    avg_r = sum(recalls) / len(recalls)
    print(f"{method_name} | Precision@{k}: {avg_p:.3f} | Recall@{k}: {avg_r:.3f}")

def main():
    employees = load_employees(DATA_DIR / "employees.csv")
    tasks = load_tasks(DATA_DIR / "tasks.csv")
    relevant_map = load_relevance(DATA_DIR / "assignments.csv")

    evaluate("Hybrid", recommend_employees, tasks, employees, relevant_map, k=3)
    evaluate("Baseline (Low Workload)", baseline_recommend, tasks, employees, relevant_map, k=3)

if __name__ == "__main__":
    main()
