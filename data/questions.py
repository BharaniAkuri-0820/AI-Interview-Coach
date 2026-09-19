CATEGORIES = {
    "Python": "Core Python concepts, syntax, and practical problem solving.",
    "Machine Learning": "Model selection, evaluation, and responsible ML fundamentals.",
    "SQL": "Queries, data modeling, and relational database reasoning.",
    "HR Interview": "Communication, teamwork, and professional self-awareness.",
    "Aptitude": "Logical reasoning, quantitative ability, and workplace problem solving.",
}


def question(prompt, options, answer, explanation, topic):
    return {"question": prompt, "options": options, "answer": answer, "explanation": explanation, "topic": topic}


QUESTIONS = {
    "Python": [
        question("Which Python type is immutable?", ["list", "dict", "set", "tuple"], "tuple", "Tuples cannot be changed after creation.", "Data types"),
        question("What does len({1, 1, 2}) return?", ["1", "2", "3", "Error"], "2", "Sets remove duplicate values.", "Data types"),
        question("Which keyword handles an exception?", ["catch", "except", "rescue", "handle"], "except", "Python uses try and except blocks.", "Exceptions"),
        question("What is a decorator used for?", ["Deleting functions", "Wrapping or extending callable behavior", "Creating variables", "Sorting lists"], "Wrapping or extending callable behavior", "Decorators modify callable behavior without changing its source.", "Decorators"),
        question("What does `==` compare?", ["Object identity", "Values", "Memory address only", "Types only"], "Values", "Equality compares values, while `is` checks identity.", "Operators"),
        question("Which structure stores key-value pairs?", ["tuple", "set", "dictionary", "string"], "dictionary", "Dictionaries map hashable keys to values.", "Data structures"),
        question("What does `yield` make a function?", ["A class", "A generator", "A decorator", "A coroutine only"], "A generator", "Yield produces values lazily from a generator function.", "Generators"),
        question("What is the first index of a Python list?", ["0", "1", "-1", "None"], "0", "Python uses zero-based indexing.", "Basics"),
        question("Which statement imports the math module?", ["include math", "using math", "import math", "require math"], "import math", "The import statement loads a module.", "Modules"),
        question("What is a list comprehension?", ["A compact list-building expression", "A list validator", "A sorting algorithm", "A class method"], "A compact list-building expression", "Comprehensions express mapping and filtering concisely.", "Syntax"),
    ],
    "Machine Learning": [
        question("What is supervised learning trained on?", ["Labeled examples", "Only random data", "No data", "Images only"], "Labeled examples", "Supervised models learn from inputs paired with target labels.", "Learning types"),
        question("Which metric is useful for imbalanced classification?", ["Accuracy only", "F1 score", "Mean only", "R-squared only"], "F1 score", "F1 balances precision and recall.", "Evaluation"),
        question("What does overfitting mean?", ["Poor training performance", "Memorizing training data and generalizing poorly", "Using too little data", "A model with no parameters"], "Memorizing training data and generalizing poorly", "Overfit models fit noise instead of general patterns.", "Generalization"),
        question("Why split data into train and test sets?", ["To increase labels", "To estimate generalization", "To remove features", "To avoid preprocessing"], "To estimate generalization", "The test set approximates performance on unseen data.", "Evaluation"),
        question("What does feature scaling help with?", ["Distance- and gradient-based models", "Text spelling", "Database joins", "Label creation"], "Distance- and gradient-based models", "Scaling prevents large-valued features dominating optimization or distance.", "Preprocessing"),
        question("What is a classification target?", ["A continuous number only", "A category or class", "A missing value", "A feature name"], "A category or class", "Classification predicts discrete labels.", "Problem types"),
        question("What does cross-validation provide?", ["Multiple estimates of model performance", "More production data", "A database schema", "A neural network"], "Multiple estimates of model performance", "It evaluates across several train-validation splits.", "Evaluation"),
        question("What is regularization designed to reduce?", ["Model complexity and overfitting", "Training examples", "Feature names", "Target labels"], "Model complexity and overfitting", "Penalties discourage overly complex parameter values.", "Generalization"),
        question("What is precision?", ["Correct positives divided by predicted positives", "Correct positives divided by all actual positives", "Correct negatives only", "All correct predictions"], "Correct positives divided by predicted positives", "Precision measures how many predicted positives were correct.", "Metrics"),
        question("What is an epoch in neural network training?", ["One pass through the training data", "One feature", "One output neuron", "One test row"], "One pass through the training data", "An epoch processes the complete training set once.", "Deep learning"),
    ],
    "SQL": [
        question("Which clause filters rows?", ["ORDER BY", "WHERE", "GROUP BY", "SELECT"], "WHERE", "WHERE filters rows before grouping.", "Queries"),
        question("Which command reads data?", ["SELECT", "INSERT", "DELETE", "ALTER"], "SELECT", "SELECT retrieves columns and rows.", "Queries"),
        question("What does a primary key provide?", ["Unique row identity", "Duplicate rows", "Automatic backups", "Encryption"], "Unique row identity", "A primary key uniquely identifies each row.", "Data modeling"),
        question("Which join keeps all rows from the left table?", ["INNER JOIN", "RIGHT JOIN", "LEFT JOIN", "CROSS JOIN"], "LEFT JOIN", "A left join preserves unmatched left-table rows.", "Joins"),
        question("Which function counts rows?", ["SUM", "COUNT", "AVG", "ROUND"], "COUNT", "COUNT returns the number of rows or non-null values.", "Aggregates"),
        question("Which clause sorts results?", ["SORT", "ORDER BY", "ARRANGE", "GROUP"], "ORDER BY", "ORDER BY sorts one or more expressions.", "Queries"),
        question("What does normalization reduce?", ["Data redundancy", "Query meaning", "Primary keys", "Indexes always"], "Data redundancy", "Normalization structures related data to reduce duplication.", "Data modeling"),
        question("Which constraint prevents NULL values?", ["UNIQUE", "NOT NULL", "CHECK", "DEFAULT"], "NOT NULL", "NOT NULL requires a value.", "Constraints"),
        question("What does GROUP BY do?", ["Groups rows for aggregation", "Deletes groups", "Renames tables", "Creates indexes"], "Groups rows for aggregation", "GROUP BY forms groups used by aggregate functions.", "Aggregates"),
        question("What is an index used for?", ["Faster lookups", "Storing passwords", "Replacing tables", "Preventing all updates"], "Faster lookups", "Indexes speed reads at the cost of storage and write overhead.", "Performance"),
    ],
    "HR Interview": [
        question("What is the strongest answer to 'Tell me about yourself'?", ["A personal life story", "A concise role-relevant career summary", "Only a salary request", "A one-word answer"], "A concise role-relevant career summary", "Connect your experience and strengths to the target role.", "Communication"),
        question("How should you discuss a weakness?", ["Deny having one", "Name a real area and show an improvement plan", "Blame a colleague", "Give no example"], "Name a real area and show an improvement plan", "Self-awareness plus action demonstrates growth.", "Self-awareness"),
        question("What does STAR stand for?", ["Situation, Task, Action, Result", "Skill, Test, Answer, Review", "Summary, Timing, Aim, Role", "Start, Try, Assess, Repeat"], "Situation, Task, Action, Result", "STAR gives behavioral answers a clear structure.", "Communication"),
        question("What should you do when you disagree with a teammate?", ["Escalate immediately", "Listen, discuss evidence, and align on a solution", "Ignore them", "End the project"], "Listen, discuss evidence, and align on a solution", "Professional disagreement focuses on outcomes, not personalities.", "Teamwork"),
        question("Why ask questions at the end of an interview?", ["To show curiosity and evaluate fit", "To avoid answering", "To negotiate before meeting", "It is required"], "To show curiosity and evaluate fit", "Thoughtful questions show preparation and mutual evaluation.", "Preparation"),
        question("What makes feedback useful?", ["It is specific and actionable", "It is always positive", "It is anonymous only", "It avoids examples"], "It is specific and actionable", "Useful feedback explains behavior, impact, and next steps.", "Growth"),
        question("How should you respond to a missed deadline?", ["Hide it", "Explain early, own the impact, and propose a recovery plan", "Blame tools", "Stop communicating"], "Explain early, own the impact, and propose a recovery plan", "Accountability and communication protect team trust.", "Accountability"),
        question("What is active listening?", ["Waiting silently", "Understanding, clarifying, and reflecting back", "Interrupting often", "Agreeing with everything"], "Understanding, clarifying, and reflecting back", "Listening includes checking understanding.", "Communication"),
        question("What should a good goal include?", ["A measurable outcome and timeframe", "Only ambition", "No deadline", "A vague slogan"], "A measurable outcome and timeframe", "Specific measurable goals make progress visible.", "Planning"),
        question("How do you handle pressure?", ["Explain prioritization and communication with an example", "Claim pressure never affects you", "Avoid the question", "Criticize managers"], "Explain prioritization and communication with an example", "Evidence of a repeatable process is more credible than a claim.", "Resilience"),
    ],
    "Aptitude": [
        question("If 20% of x is 30, what is x?", ["60", "120", "150", "180"], "150", "30 / 0.20 = 150.", "Percentages"),
        question("What is the next number: 2, 4, 8, 16, ?", ["20", "24", "32", "36"], "32", "Each term doubles.", "Sequences"),
        question("A train travels 60 km in 1.5 hours. Its speed is:", ["30 km/h", "40 km/h", "45 km/h", "90 km/h"], "40 km/h", "Speed = distance / time = 60 / 1.5.", "Time and distance"),
        question("What is the average of 8, 10, and 12?", ["9", "10", "11", "12"], "10", "The sum is 30 and 30 / 3 = 10.", "Averages"),
        question("If a:b = 2:3 and b = 12, a equals:", ["6", "8", "9", "18"], "8", "Scale the ratio by 4: 2 x 4 = 8.", "Ratios"),
        question("What is 15% of 200?", ["15", "20", "30", "35"], "30", "200 x 0.15 = 30.", "Percentages"),
        question("A $100 item with 10% discount costs:", ["$80", "$90", "$95", "$110"], ["$90"][0], "The discount is $10, leaving $90.", "Percentages"),
        question("If all analysts are learners and Sam is an analyst, Sam is:", ["A manager", "A learner", "Not an analyst", "Unknown"], "A learner", "This follows directly from the stated inclusion.", "Logic"),
        question("How many minutes are in 2.5 hours?", ["120", "150", "180", "250"], "150", "2.5 x 60 = 150 minutes.", "Conversions"),
        question("A project has 4 tasks taking 3 hours each in sequence. Total time?", ["7 hours", "12 hours", "16 hours", "24 hours"], "12 hours", "Four sequential tasks take 4 x 3 hours.", "Work rates"),
    ],
}
