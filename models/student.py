class Student:
    def __init__(self, sid, name, marks, attendance):
        self.sid = sid
        self.name = name
        self.marks = marks
        self.attendance = attendance

    def average(self):
        return sum(self.marks.values()) / len(self.marks) if self.marks else 0

    def to_dict(self):
        return {
            "id": self.sid,
            "name": self.name,
            "marks": self.marks,
            "attendance": self.attendance
        }

    @staticmethod
    def from_dict(d):
        return Student(d["id"], d["name"], d["marks"], d["attendance"])