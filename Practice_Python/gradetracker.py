# Create a Student class that:
# - Keeps track of grades for different subjects
# - Can add new grades for a subject
# - Can calculate average grade per subject
# - Can calculate overall GPA
# - Can show the highest grade and which subject it was in

# Example usage:
student = Student("Maria")
student.add_grade("Math", 95)
student.add_grade("Math", 88)
student.add_grade("Science", 92)
student.subject_average("Math")    # Should return 91.5
student.get_highest_grade()        # Should show the highest grade and subject
student.calculate_gpa()            # Should calculate overall average