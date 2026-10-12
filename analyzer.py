import csv
import os

def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

folder = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(folder, "students.csv")

all_students = []

with open(filepath, "r") as file:
    reader = csv.DictReader(file)
    for student in reader:
        python = int(student["python"])
        sql = int(student["sql"])
        math = int(student["math"])
        average = round((python + sql + math) / 3, 2)
        grade = get_grade(average)
        print(student["name"], "Average:", average, "Grade:", grade)
        all_students.append({
            "name": student["name"],
            "average": average,
            "grade": grade,
            "attendence": int(student["attendence"])
        })

topper = max(all_students, key=lambda s: s["average"])
weakest = min(all_students, key=lambda s: s["average"])

print("\n--- Result ---")
print("Topper:", topper["name"], "Average:", topper["average"])
print("Weakest:", weakest["name"], "Average:", weakest["average"])

output_path = os.path.join(folder, "results.csv")
with open(output_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "average", "grade", "attendence"])
    writer.writeheader()
    writer.writerows(all_students)

print("Results saved to results.csv")


def show_all():
    for s in all_students:
        print(s["name"], "Average:", s["average"], "Grade:", s["grade"])

def search_student():
    name = input("Enter student name: ").strip().lower()
    found = False
    for s in all_students:
        if s["name"].lower() == name:
            print(s["name"], "Average:", s["average"], "Grade:", s["grade"])
            found = True
    if not found:
        print("Student not found")

def top_three():
    top = sorted(all_students, key=lambda s: s["average"], reverse=True)[:3]
    for i, s in enumerate(top, 1):
        print(i, s["name"], "Average:", s["average"], "Grade:", s["grade"])

def low_attendence():
    print("\nStudents with attendence below 75%:")
    found = False
    for s in all_students:
        if s["attendence"] < 75:
            print(s["name"], "Attendence:", s["attendence"])
            found = True
    if not found:
        print("All students have good attendence!")


while True:
    print("\n--- MENU ---")
    print("1. View all students")
    print("2. Search by name")
    print("3. Top 3 students")
    print("4. Low attendence students")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        show_all()
    elif choice == "2":
        search_student()
    elif choice == "3":
        top_three()
    elif choice == "4":
        low_attendence()
    elif choice == "5":
        print("Bye!")
        break
    else:
        print("Invalid choice")