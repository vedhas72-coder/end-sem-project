import json
from models.student import Student

FILE = "students.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
            return [Student.from_dict(d) for d in data]
    except:
        return []

def save_data(students):
    with open(FILE, "w") as f:
        json.dump([s.to_dict() for s in students], f, indent=4)