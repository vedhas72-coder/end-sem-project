def calculate_average(marks):
    return sum(marks.values()) / len(marks) if marks else 0


def generate_remark(avg):
    if avg >= 85:
        return "Excellent performance!"
    elif avg >= 70:
        return "Very good performance!"
    elif avg >= 50:
        return "Good, but can improve."
    elif avg >= 40:
        return "Needs improvement."
    else:
        return "Poor performance. Work harder."