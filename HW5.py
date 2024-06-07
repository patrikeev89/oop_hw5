class Teacher:
    def __init__(self, teacher_id: int, name: str):
        self.teacher_id = teacher_id
        self.name = name

class Student:
    def __init__(self, student_id: int, name: str):
        self.student_id = student_id
        self.name = name

class StudyGroup:
    def __init__(self, teacher: Teacher, students: list[Student]):
        self.teacher = teacher
        self.students = students

    def __str__(self):
        return f"Teacher: {self.teacher.name}, Students: {[student.name for student in self.students]}"

class StudyGroupService:
    @staticmethod
    def create_study_group(teacher: Teacher, students: list[Student]) -> StudyGroup:
        return StudyGroup(teacher, students)

class Controller:
    def __init__(self, student_service, teacher_service, study_group_service):
        self.student_service = student_service
        self.teacher_service = teacher_service
        self.study_group_service = study_group_service

    def form_study_group(self, teacher_id: int, student_ids: list[int]) -> StudyGroup:
        teacher = self.teacher_service.get_teacher_by_id(teacher_id)
        students = self.student_service.get_students_by_ids(student_ids)
        study_group = self.study_group_service.create_study_group(teacher, students)
        return study_group

class TeacherService:
    def __init__(self, teachers: list[Teacher]):
        self.teachers = teachers

    def get_teacher_by_id(self, teacher_id: int) -> Teacher:
        for teacher in self.teachers:
            if teacher.teacher_id == teacher_id:
                return teacher
        raise ValueError("Учитель не найден")

class StudentService:
    def __init__(self, students: list[Student]):
        self.students = students

    def get_students_by_ids(self, student_ids: list[int]) -> list[Student]:
        found_students = []
        for student_id in student_ids:
            for student in self.students:
                if student.student_id == student_id:
                    found_students.append(student)
                    break
        if len(found_students) != len(student_ids):
            raise ValueError("Студенты не найдены")
        return found_students

# Данные
teachers = [
    Teacher(1, "Иванов Иван Иванович"),
    Teacher(2, "Петров Петр Петрович")
]

students = [
    Student(1, "Александр"),
    Student(2, "Ольга"),
    Student(3, "Андрей")
]

# Создание сервисов
teacher_service = TeacherService(teachers)
student_service = StudentService(students)
study_group_service = StudyGroupService()

# Создание контроллера
controller = Controller(student_service, teacher_service, study_group_service)

# Создание учебной группы
try:
    study_group = controller.form_study_group(2, [1, 3])
    print(study_group)
except ValueError as e:
    print(e)
