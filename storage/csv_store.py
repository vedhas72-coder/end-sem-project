import csv
from utils.helpers import calculate_average

def export_csv(students):
    with open("report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Average", "Attendance"])

        for s in students:
            writer.writerow([
                s.sid,
                s.name,
                calculate_average(s.marks),
                round(s.attendance, 2)
            ])

    print("CSV Exported successfully!")