import os

from openai import OpenAI


def evaluate_practice(topic, difficulty, answer):
    answer_length = len(answer.split())
    if not answer.strip():
        return {"correctness": "No answer submitted", "clarity": "Add a structured response", "technical": "No evidence yet", "improvement": "Answer the question using a definition and a concrete example.", "better_answer": "Start with the core idea, explain why it matters, and finish with a practical example."}
    if os.getenv("OPENAI_API_KEY"):
        try:
            client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
            response = client.responses.create(
                model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
                input=(
                    f"Evaluate this {difficulty} {topic} interview answer. Return concise feedback with "
                    "correctness, clarity, technical knowledge, improvement, and better_answer labels.\n\n"
                    f"Answer: {answer}"
                ),
            )
            return {"correctness": "AI review available", "clarity": response.output_text, "technical": "See the detailed review", "improvement": "Use the review to revise your answer.", "better_answer": "Rewrite the answer using the suggested structure and a concrete example."}
        except Exception:
            pass
    clarity = "Clear and concise" if answer_length <= 120 else "Consider a shorter, more focused response"
    quality = "Strong foundation" if answer_length >= 20 else "Add more detail and an example"
    return {"correctness": f"Good direction for a {difficulty.lower()} {topic} response.", "clarity": clarity, "technical": quality, "improvement": "Use a simple structure: concept, reasoning, and example.", "better_answer": "Define the idea, mention an important trade-off, and connect it to a real project or workplace situation."}
