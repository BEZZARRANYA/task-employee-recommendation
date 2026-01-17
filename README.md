# Task-to-Employee Recommendation System (Hybrid)

This project recommends the best employee(s) for a given task using a hybrid scoring approach:
- Skill similarity (task requirements vs employee skills)
- Performance history (ratings / success)
- Workload & availability constraints

## Motivation
In real organizations, assigning tasks to the right employee affects efficiency and quality.  
This project explores an explainable, practical recommendation approach that can be integrated into a management system.

## Project Structure
- `data/` example datasets (synthetic)
- `src/` recommendation logic
- `notebooks/` experiments and evaluation (to be added)

## Next Steps
- Add synthetic datasets (`employees.csv`, `tasks.csv`, `assignments.csv`)
- Implement hybrid scoring in `src/recommend.py`
- Add evaluation metrics (Precision@K)
