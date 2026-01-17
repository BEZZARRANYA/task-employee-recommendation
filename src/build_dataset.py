import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

def load_employees(path):
    employees = {}
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            employees[row["employee_id"]] = row
    return employees

def load_tasks(path):
    tasks = {}
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tasks[row["task_id"]] = row
    return tasks

def build_dataset():
    employees = load_employees(DATA_DIR / "employees.csv")
    tasks = load_tasks(DATA_DIR / "tasks.csv")

    rows = []
    with open(DATA_DIR / "assignments.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for a in reader:
            emp = employees[a["employee_id"]]
            task = tasks[a["task_id"]]

            emp_skills = set(s.strip() for s in emp["skills"].split(","))
            task_skills = set(s.strip() for s in task["required_skills"].split(","))

            matching_skills = emp_skills & task_skills
            skill_match_ratio = (
                len(matching_skills) / len(task_skills)
                if len(task_skills) > 0 else 0.0
            )

            rows.append({
                "experience_years": float(emp["experience_years"]),
                "avg_rating": float(emp["avg_rating"]),
                "current_workload": float(emp["current_workload"]),
                "availability": int(emp["availability"]),
                "task_priority": int(task["priority"]),
                "estimated_hours": float(task["estimated_hours"]),
                "skill_match_ratio": skill_match_ratio,
                "success": int(a["success"])
            })

    return rows

if __name__ == "__main__":
    data = build_dataset()
    for row in data[:5]:
        print(row)
             

