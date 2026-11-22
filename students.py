students = [
    {"name": "Alex", "grade": 4},
    {"name": "Maria", "grade": 5, "status": "excellent"}
]


def show_students():
    for student in students:
        print(student["name"], student["grade"])


show_students()
