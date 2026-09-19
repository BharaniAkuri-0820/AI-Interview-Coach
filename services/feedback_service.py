def performance_level(percentage):
    if percentage >= 85:
        return "Excellent"
    if percentage >= 70:
        return "Good"
    if percentage >= 50:
        return "Average"
    return "Needs Improvement"


def build_feedback(category, answers, questions):
    wrong_topics = [item["topic"] for item in answers if not item["is_correct"]]
    right_topics = [item["topic"] for item in answers if item["is_correct"]]
    percentage = round(sum(item["is_correct"] for item in answers) / len(questions) * 100) if questions else 0
    unique_wrong = list(dict.fromkeys(wrong_topics))
    unique_right = list(dict.fromkeys(right_topics))
    if unique_wrong:
        recommendation = f"Review {', '.join(unique_wrong[:2])}, then retake a {category} test to confirm the concepts."
    else:
        recommendation = f"Keep your momentum with an advanced {category} practice session."
    return {
        "level": performance_level(percentage),
        "strong_topics": unique_right[:3] or ["Keep practicing to build a strength"],
        "weak_topics": unique_wrong[:3] or ["No major gaps identified"],
        "readiness": "Interview ready" if percentage >= 70 else "Building confidence",
        "recommendation": recommendation,
    }
