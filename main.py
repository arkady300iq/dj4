import django_setup

from myapp.models import Class, Subject, Teacher, Student, Schedule, Grade


def add_class_to_db(name):
    clas = Class(
        name = name
    )
    clas.save()
    
    return clas


def add_subject_to_db(name):
    subject = Subject(
        name = name
    )
    subject.save()

    return subject


def add_teacher_to_db(name, surname):
    teacher = Teacher(
        name = name,
        surname = surname
    )
    teacher.save()

    return teacher


def add_student_to_db(name, surname):
    student = Student(
        name = name,
        surname = surname
    )
    student.save()

    return student


def sign_student_on_class(student_id, class_id):
    student = Student.objects.get(id = student_id)
    clas = Class.objects.get(id = class_id)
    student.classes.add(clas)


def specialize_teacher_to_current_subject(teacher_id, subject_id):
    teacher = Teacher.objects.get(id = teacher_id)
    subject = Subject.objects.get(id = subject_id)
    teacher.subject.add(subject)


def add_subject_to_schedule(name_clas, subjects, teacher):
    schedule = Schedule(
        name_clas = name_clas,
        subjects = subjects,
        teacher = teacher
    )
    schedule.save()

    return schedule


def add_grade_to_student(grade, student, schedule):
    mark = Grade(
        grade = grade,
        student = student,
        schedule = schedule
    )

    mark.save()

    return mark


def main():
    while True:
        question = int(input("Register new class - 1\nAdd new subject - 2\nRegister new teacher - 3\nRegister new student - 4\nSign student to new class - 5\nSpecialize teacher with a subject - 6\nAdd subject to schedule - 7\nAdd grade to student - 8\nExit - 0\n"))

        match question:
            case 1:
                name = input("Enter name of class:")
                print(add_class_to_db(name))
            
            case 2:
                name = input("Enter name of subject:")
                print(add_subject_to_db(name))

            case 3:
                name = input("Enter teacher's name:")
                surname = input("Enter teacher's surname:")
                print(add_teacher_to_db(name, surname))

            case 4:
                name = input("Enter student's name:")
                surname = input("Enter student's surname:")
                print(add_student_to_db(name, surname))

            case 5:
                student_id = input("Enter student's id:")
                class_id = input("Enter class's id:")
                print(sign_student_on_class(student_id, class_id))

            case 6:
                teacher_id = input("Enter teacher's id:")
                subject_id = input("Enter subject's id:")
                print(specialize_teacher_to_current_subject(teacher_id, subject_id))

            case 7:
                clas = int(input("Class_Id: "))
                subjects = int(input("Subjects_id: "))
                teacher = int(input("Teacher_id: "))
                print(add_subject_to_schedule(clas, subjects, teacher))

            case 8:
                grade = int(input("Grade: "))
                student = int(input("Student id: "))
                schedule = int(input("Schedule id: "))
                print(add_grade_to_student(grade, student, schedule))

            case 0:
                break




if __name__ == "__main__":
    main()