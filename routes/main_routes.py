from flask import Blueprint, redirect, render_template, request, session, url_for

from app import db
from data.questions import CATEGORIES
from models.database_models import TestAttempt, User

main_bp = Blueprint("main", __name__)


def current_user():
    user = User.query.get(session.get("user_id")) if session.get("user_id") else None
    if not user:
        user = User.query.first()
        session["user_id"] = user.id
    return user


@main_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if name:
            user = current_user()
            user.name = name
            user.email = request.form.get("email", "").strip() or user.email
            db.session.commit()
            return redirect(url_for("main.dashboard"))
    return render_template("index.html", categories=CATEGORIES)


@main_bp.route("/categories")
def categories():
    return render_template("categories.html", categories=CATEGORIES)


@main_bp.route("/dashboard")
def dashboard():
    user = current_user()
    attempts = TestAttempt.query.filter_by(user_id=user.id).order_by(TestAttempt.date.desc()).all()
    average = round(sum(a.percentage for a in attempts) / len(attempts)) if attempts else 0
    best = max((a.percentage for a in attempts), default=0)
    strengths = attempts[0].category if attempts else "Take your first test"
    return render_template("dashboard.html", user=user, attempts=attempts[:5], total=len(attempts), average=average, best=round(best), strengths=strengths, categories=CATEGORIES)


@main_bp.route("/profile", methods=["POST"])
def profile():
    user = current_user()
    user.name = request.form.get("name", user.name).strip() or user.name
    db.session.commit()
    return redirect(url_for("main.dashboard"))
