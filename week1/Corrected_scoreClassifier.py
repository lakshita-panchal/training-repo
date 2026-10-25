def get_grade_category(score: float) -> str:
    """Maps a validated numeric score to its corresponding grade category."""
    if score >= 90:
        return "A (Excellent)"
    if score >= 80:
        return "B (Very Good)"
    if score >= 70:
        return "C (Good)"
    if score >= 50:
        return "D (Pass)"
    return "F (Fail)"


def validate_and_process_grades():
    """Iterates through student records, enforces valid score ranges, and outputs grades."""
    student_records = [
        {"name": "Amit", "score": 92},
        {"name": "Priya", "score": 78},
        {"name": "Rohan", "score": 145},
        {"name": "Sneha", "score": 45},
        {"name": "Vikram", "score": -10},
    ]

    print("--- Student Grade Classification ---")

    for record in student_records:
        student_name = record["name"]
        current_score = record["score"]

        # Loop guarantees execution continues only after getting a 0-100 score
        while not (0 <= current_score <= 100):
            print(
                f"[Error] {student_name} has an invalid score of {current_score}. Range must be 0-100."
            )
            try:
                current_score = float(
                    input(f"Enter corrected score for {student_name}: ")
                )
            except ValueError:
                print("Invalid input. Please enter a number.")
                current_score = -1

        assigned_grade = get_grade_category(current_score)
        print(
            f"Student: {student_name} | Score: {current_score} | Grade: {assigned_grade}"
        )
        print("-" * 40)


if __name__ == "__main__":
    validate_and_process_grades()

