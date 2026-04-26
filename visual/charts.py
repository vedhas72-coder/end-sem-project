import matplotlib.pyplot as plt
from utils.helpers import calculate_average

def bar_chart(student):
    subjects = list(student.marks.keys())
    marks = list(student.marks.values())

    plt.bar(subjects, marks)
    plt.title(student.name + " - Subject Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.show()


def pie_chart(student):
    present = student.attendance
    absent = 100 - present

    plt.pie([present, absent], labels=["Present", "Absent"], autopct="%1.1f%%")
    plt.title(student.name + " - Attendance")
    plt.show()


def histogram(students):
    avgs = [calculate_average(s.marks) for s in students if s.marks]

    if not avgs:
        print("No data available")
        return

    plt.hist(avgs)
    plt.title("Class Performance Distribution")
    plt.xlabel("Average Marks")
    plt.ylabel("Number of Students")
    plt.show()