import csv
from pathlib import Path
from recommend import recommend_employees

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

def main():
    employees = load_employees(DATA_DIR / "employees.csv")
    tasks = load_tasks(DATA_DIR / "tasks.csv")

    task = tasks["T01"]  # Build API
    recs = recommend_employees(task, employees, top_k=3)

    print(f"Task: {task['title']} | Required skills: {task['required_skills']}")
    print("Top recommendations:")
    for i, emp in enumerate(recs, start=1):
        print(f"{i}. {emp['name']} ({emp['employee_id']}) - skills={emp['skills']} rating={emp['avg_rating']} workload={emp['current_workload']} availability={emp['availability']}")

if __name__ == "__main__":
    main()
