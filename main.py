from models.student import Student
from storage.json_store import load_data, save_data
from storage.csv_store import export_csv
from utils.helpers import calculate_average, generate_remark
from analysis.stats import class_average, class_median, class_variance
from visual.charts import bar_chart, pie_chart, histogram


def find_student(students, sid):
    for s in students:
        if s.sid == sid:
            return s
    return None


def display_student(s):
    avg = calculate_average(s.marks)

    print("\n--- Student Details ---")
    print("ID:", s.sid)
    print("Name:", s.name)
    print("Marks:", s.marks)
    print("Attendance:", round(s.attendance, 2), "%")
    print("Average:", round(avg, 2))
    print("Remark:", generate_remark(avg))

    if s.attendance < 50:
        print(" Low Attendance Alert!")


def main():
    students = load_data()

    while True:
        print("\n===== SAPAS MENU =====")
        print("1. Add Student")
        print("2. View All")
        print("3. Search")
        print("4. Delete")
        print("5. Topper")
        print("6. Update")
        print("7. Analytics")
        print("8. Graphs")
        print("9. Export CSV")
        print("10. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            sid = input("ID: ")
            name = input("Name: ")

            n = int(input("Number of subjects: "))
            marks = {}
            for _ in range(n):
                sub = input("Subject: ")
                marks[sub] = float(input("Marks: "))

            p = int(input("Days present: "))
            t = int(input("Total days: "))
            att = (p / t) * 100 if t > 0 else 0

            students.append(Student(sid, name, marks, att))
            print("Student added!")

        elif ch == "2":
            for s in students:
                display_student(s)

        elif ch == "3":
            s = find_student(students, input("Enter ID: "))
            display_student(s) if s else print("Not found")

        elif ch == "4":
            sid = input("Enter ID: ")
            students = [s for s in students if s.sid != sid]
            print("Deleted!")

        elif ch == "5":
            if students:
                top = max(students, key=lambda s: s.average())
                display_student(top)

        elif ch == "6":
            s = find_student(students, input("Enter ID: "))
            if s:
                s.name = input("New Name: ")
                print("Updated!")

        elif ch == "7":
            print("Class Average:", class_average(students))
            print("Median:", class_median(students))
            print("Variance:", class_variance(students))

        elif ch == "8":
            print("1.Bar 2.Pie 3.Histogram")
            g = input("Choice: ")

            if g == "1":
                s = find_student(students, input("Enter ID: "))
                if s: bar_chart(s)

            elif g == "2":
                s = find_student(students, input("Enter ID: "))
                if s: pie_chart(s)

            elif g == "3":
                histogram(students)

        elif ch == "9":
            export_csv(students)

        elif ch == "10":
            save_data(students)
            print("Saved & Exit")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()