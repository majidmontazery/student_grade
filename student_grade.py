# Initialize dictionaries
student_scores = {}
student_grades = {}

# Get the number of students
num_students = int(input("Enter the number of students: "))

# Get all student names
names = input("Enter the students' names separated by spaces: ").split()

# Get all student scores
scores = input("Enter the scores for the students separated by spaces: ").split()

# Check if the number of names matches the number of scores
if len(names) != num_students or len(scores) != num_students:
    print("Error: The number of names and scores must match the number of students!")
else:
    # Convert scores to integers and populate the dictionary
    for i in range(num_students):
        student_scores[names[i]] = int(scores[i])

    # Calculate grades
    for student in student_scores:
        score = student_scores[student]
        if score > 90:
            student_grades[student] = "Outstanding"
        elif score > 80:
            student_grades[student] = "Exceeds Expectations"
        elif score > 70:
            student_grades[student] = "Acceptable"
        else:
            student_grades[student] = "Fail"

    # Print the student grades dictionary
    print("\nStudent Grades:")
    print(student_grades)
