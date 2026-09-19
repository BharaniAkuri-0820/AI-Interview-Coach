from datetime import datetime

from flask import Blueprint, redirect, render_template, request, session, url_for

from app import db
from data.questions import CATEGORIES, QUESTIONS
from models.database_models import TestAttempt, UserAnswer
from routes.main_routes import current_user
from services.feedback_service import build_feedback

quiz_bp = Blueprint("quiz", __name__, url_prefix="/quiz")


@quiz_bp.route("/<category>")
def start(category):
    if category not in QUESTIONS:
        return redirect(url_for("main.categories"))
    session["quiz_category"] = category
    session["quiz_answers"] = {}
    return render_template("quiz.html", category=category, questions=QUESTIONS[category], duration=1800, description=CATEGORIES[category])


@quiz_bp.route("/<category>/submit", methods=["POST"])
def submit(category):
    questions = QUESTIONS.get(category)
    if not questions:
        return redirect(url_for("main.categories"))
    answers = request.form.to_dict(flat=True)
    reviewed = []
    for index, item in enumerate(questions):
        selected = answers.get(f"question_{index}")
        reviewed.append({"question": item["question"], "selected_answer": selected, "correct_answer": item["answer"], "is_correct": selected == item["answer"], "explanation": item["explanation"], "topic": item["topic"]})
    score = sum(item["is_correct"] for item in reviewed)
    percentage = round(score / len(questions) * 100)
    user = current_user()
    attempt = TestAttempt(user_id=user.id, category=category, score=score, total_questions=len(questions), percentage=percentage, date=datetime.utcnow())
    db.session.add(attempt)
    db.session.flush()
    for item in reviewed:
        db.session.add(UserAnswer(attempt_id=attempt.id, question=item["question"], selected_answer=item["selected_answer"], correct_answer=item["correct_answer"], is_correct=item["is_correct"]))
    db.session.commit()
    feedback = build_feedback(category, reviewed, questions)
    return render_template("result.html", attempt=attempt, reviewed=reviewed, feedback=feedback)
