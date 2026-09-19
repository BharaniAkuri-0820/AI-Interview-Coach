import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-change-me")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///interview_coach.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    from routes.main_routes import main_bp
    from routes.quiz_routes import quiz_bp
    from routes.interview_routes import interview_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(quiz_bp)
    app.register_blueprint(interview_bp)

    with app.app_context():
        from models.database_models import User
        db.create_all()
        if not User.query.first():
            db.session.add(User(name="Demo Candidate", email="demo@example.com"))
            db.session.commit()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
