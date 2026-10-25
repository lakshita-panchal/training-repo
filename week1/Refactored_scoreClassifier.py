def classify_score(score):
    if score >= 90:
        return "A (Excellent)"
    elif score >= 80:
        return "B (Very Good)"
    elif score >= 70:
        return "C (Good)"
    elif score >= 50:
        return "D (Pass)"
    else:
        return "F (Fail)"


def process_students():
    students = [
        {"name": "Amit", "score": 92},
        {"name": "Priya", "score": 78},
        {"name": "Rohan", "score": 145},
        {"name": "Sneha", "score": 45},
        {"name": "Vikram", "score": -10},
    ]

    print("--- Student Grade Classification ---")

    for student in students:
        name = student["name"]
        score = student["score"]

        while score < 0 or score > 100:
            print(
                f"[Error] {name} has an invalid score of {score}. Must be between 0 and 100."
            )
            try:
                score = float(
                    input(f"Enter a corrected numeric score for {name}: ")
                )
            except ValueError:
                print("Please enter a valid number.")
                score = -1

        grade = classify_score(score)
        print(f"Student: {name} | Score: {score} | Grade: {grade}")
        print("-" * 40)


if __name__ == "__main__":
    process_students()

