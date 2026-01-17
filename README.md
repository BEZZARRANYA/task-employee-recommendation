# Task-to-Employee Recommendation System (Hybrid)

This project recommends the best employee(s) for a given task using a hybrid scoring approach that integrates:
- Skill similarity (task requirements vs. employee skills)
- Historical performance (ratings and successful assignments)
- Workload and availability constraints

## Motivation
In real organizations, assigning tasks to appropriate employees directly affects efficiency and quality.  
This project explores an **explainable and practical recommendation approach** that can be integrated into enterprise management systems.

## Project Structure
- `data/` synthetic datasets simulating organizational task assignments
- `src/` recommendation logic, baseline, and evaluation scripts

## Evaluation (Synthetic Historical Assignments)

We evaluate task-to-employee recommendation using **historical assignment outcomes**, where `success = 1` indicates a relevant employee for a given task.

**Metrics:** Precision@3 and Recall@3

**Results:**
- **Hybrid (skills + performance + workload/availability):**
  - Precision@3 = **0.792**
  - Recall@3 = **0.875**
- **Baseline (lowest workload only):**
  - Precision@3 = **0.292**
  - Recall@3 = **0.292**

The hybrid approach significantly outperforms the baseline, demonstrating the effectiveness of incorporating task–skill matching and historical performance signals.

## Next Steps
- Extend evaluation with larger datasets
- Explore learning-to-rank or neural recommendation models
- Integrate the recommendation module into a full Flask-based management system
## Results (Employee Performance Prediction)

We evaluated multiple machine learning models on historical task assignment data.

| Model                | Accuracy | Precision | Recall | F1-score |
|---------------------|----------|-----------|--------|----------|
| Logistic Regression | 0.625    | 0.833     | 0.714  | 0.769    |
| Random Forest       | 0.875    | 0.875     | 1.000  | 0.933    |

The Random Forest model significantly outperformed the baseline Logistic Regression model, demonstrating the effectiveness of non-linear modeling and feature interaction (e.g., skill matching) in predicting task success.
