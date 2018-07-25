from hs_student import HighSchoolStudent
from student import Student
# Calling StudentClass
surya = Student("surya")
print(surya.get_name_capitalize())
print(surya.get_school_name())

# Calling Inherited class
suneel = HighSchoolStudent("suneel")
print(suneel.get_name_capitalize())
print(suneel.get_school_name())