from flask import Blueprint, render_template, request

from data.questions import CATEGORIES
from services.ai_service import evaluate_practice

interview_bp = Blueprint("interview", __name__, url_prefix="/practice")


@interview_bp.route("/", methods=["GET", "POST"])
def practice():
    feedback = None
    prompt = None
    topic = request.form.get("topic", "Python")
    difficulty = request.form.get("difficulty", "Intermediate")
    if request.method == "POST":
        prompt = f"Explain a practical {topic} concept you would expect at {difficulty.lower()} level, and give an example."
        feedback = evaluate_practice(topic, difficulty, request.form.get("answer", ""))
    return render_template("interview_practice.html", categories=CATEGORIES, feedback=feedback, prompt=prompt, topic=topic, difficulty=difficulty)
