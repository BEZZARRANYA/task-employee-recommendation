def baseline_recommend(task, employees, top_k=3):
    """
    Simple baseline recommender:
    Recommend available employees with the lowest workload.
    """
    available = [e for e in employees if int(e.get("availability", 0)) == 1]
    available.sort(key=lambda e: float(e.get("current_workload", 0)))
    return available[:top_k]
