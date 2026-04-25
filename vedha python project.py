import json
import statistics
import csv
import matplotlib.pyplot as plt

FILE = "students.json"

# ---------------- LOAD & SAVE ----------------
def load_data():
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except:
        return []

def save_data(students):
    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)


# ---------------- HELPER FUNCTIONS ----------------
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
        return "⚠ Needs improvement."
    else:
        return "❌ Poor performance. Work harder."


def find_student(students, sid):
    for s in students:
        if s["id"] == sid:
            return s
    return None


# ---------------- ANALYTICS ----------------
def class_average(students):
    avgs = [calculate_average(s["marks"]) for s in students if s["marks"]]
    return statistics.mean(avgs) if avgs else 0

def class_median(students):
    avgs = [calculate_average(s["marks"]) for s in students if s["marks"]]
    return statistics.median(avgs) if avgs else 0

def class_variance(students):
    avgs = [calculate_average(s["marks"]) for s in students if s["marks"]]
    return statistics.variance(avgs) if len(avgs) > 1 else 0


# ---------------- VISUALIZATION ----------------
def bar_chart(student):
    subjects = list(student["marks"].keys())
    marks = list(student["marks"].values())

    plt.bar(subjects, marks)
    plt.title(student["name"] + " - Subject Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.show()


def pie_chart(student):
    present = student["attendance"]
    absent = 100 - present

    plt.pie([present, absent], labels=["Present", "Absent"], autopct="%1.1f%%")
    plt.title(student["name"] + " - Attendance")
    plt.show()


def histogram(students):
    avgs = [calculate_average(s["marks"]) for s in students if s["marks"]]

    if not avgs:
        print("No data for graph")
        return

    plt.hist(avgs)
    plt.title("Class Performance Distribution")
    plt.xlabel("Average Marks")
    plt.ylabel("No. of Students")
    plt.show()


# ---------------- CSV EXPORT ----------------
def export_csv(students):
    with open("report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Average", "Attendance"])

        for s in students:
            writer.writerow([
                s["id"],
                s["name"],
                calculate_average(s["marks"]),
                round(s["attendance"], 2)
            ])

    print("✅ CSV Exported!")


# ---------------- DISPLAY ----------------
def display_student(s):
    avg = calculate_average(s["marks"])

    print("\n--- Student Details ---")
    print("ID:", s["id"])
    print("Name:", s["name"])
    print("Marks:", s["marks"])
    print("Attendance:", round(s["attendance"], 2), "%")
    print("Average:", round(avg, 2))
    print("Remark:", generate_remark(avg))

    if s["attendance"] < 50:
        print("⚠ Low Attendance Alert!")


# ---------------- MAIN ----------------
def main():
    students = load_data()

    while True:
        print("\n===== SAPAS MENU =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Top Performer")
        print("6. Update Student")
        print("7. Analytics")
        print("8. Graphs")
        print("9. Export CSV")
        print("10. Save Data")
        print("11. Exit")

        choice = input("Enter your choice: ")

        # -------- ADD STUDENT --------
        if choice == "1":
            sid = input("Enter Student ID: ")
            name = input("Enter Name: ")

            n = int(input("Enter number of subjects: "))
            marks = {}
            for _ in range(n):
                sub = input("Enter subject: ")
                marks[sub] = float(input("Enter marks: "))

            present = int(input("Days present: "))
            total = int(input("Total days: "))
            attendance = (present / total) * 100 if total > 0 else 0

            students.append({
                "id": sid,
                "name": name,
                "marks": marks,
                "attendance": attendance
            })

            print("Student added!")

        # -------- VIEW --------
        elif choice == "2":
            for s in students:
                display_student(s)

        # -------- SEARCH --------
        elif choice == "3":
            s = find_student(students, input("Enter ID: "))
            display_student(s) if s else print("Not found")

        # -------- DELETE --------
        elif choice == "4":
            sid = input("Enter ID: ")
            students = [s for s in students if s["id"] != sid]
            print("Deleted!")

        # -------- TOPPER --------
        elif choice == "5":
            if students:
                top = max(students, key=lambda s: calculate_average(s["marks"]))
                display_student(top)

        # -------- UPDATE --------
        elif choice == "6":
            s = find_student(students, input("Enter ID: "))
            if s:
                s["name"] = input("New name: ")

                n = int(input("Subjects count: "))
                marks = {}
                for _ in range(n):
                    sub = input("Subject: ")
                    marks[sub] = float(input("Marks: "))
                s["marks"] = marks

                present = int(input("Days present: "))
                total = int(input("Total days: "))
                s["attendance"] = (present / total) * 100 if total > 0 else 0

                print("Updated!")

        # -------- ANALYTICS --------
        elif choice == "7":
            print("Class Average:", class_average(students))
            print("Median:", class_median(students))
            print("Variance:", class_variance(students))

        # -------- GRAPHS --------
        elif choice == "8":
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

        # -------- CSV --------
        elif choice == "9":
            export_csv(students)

        # -------- SAVE --------
        elif choice == "10":
            save_data(students)
            print("Saved!")

        # -------- EXIT --------
        elif choice == "11":
            save_data(students)
            print("Exiting...")
            break

        else:
            print("Invalid choice")


# -------- RUN --------
if __name__ == "__main__":
    main()