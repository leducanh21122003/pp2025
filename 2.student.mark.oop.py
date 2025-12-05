class Student:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.dob = ""

    def input(self):
        print("\n--- NHẬP THÔNG TIN SINH VIÊN ---")
        self.id = input("Nhập ID sinh viên: ")
        self.name = input("Nhập tên sinh viên: ")
        self.dob = input("Nhập ngày sinh (dd/mm/yyyy): ")
        
    def __str__(self)   :
        return f"ID: {self.id} | Name: {self.name} | DOB: {self. dob}"

class Course:   
    def __init__ (self):
        print("\n--- NHẬP THÔNG TIN MÔN HỌC ---")
        self.id = input("Nhập ID môn học: ")
        self.name = input("Nhập tên môn học: ")

    def __str__(self):
        return f"ID: {self.id} | Name: {self.name}"

class SchoolManagement:
    def __init__(self):
        self.students = [] 
        self.courses = []
        self.marks = {} 

    def input_students(self):
        count = int(input("\nNhập số lượng sinh viên: "))
        for _ in range(count):
            student = Student()
            student.input() 
            self.students.append(student)

    def input_courses(self):
        count = int(input("\nNhập số lượng môn học: "))
        for _ in range(count):
            course = Course()
            course.input()
            self.courses.append(course)

    def list_students(self):
        print("\n--- DANH SÁCH SINH VIÊN ---")
        for s in self.students:
            print(s) 

    def list_courses(self):
        print("\n--- DANH SÁCH MÔN HỌC ---")
        for c in self.courses:
            print(c) 

    def input_marks(self):
        print("\n--- NHẬP ĐIỂM ---")
        self.list_courses()
        course_id = input("Chọn ID môn học để nhập điểm: ")
        
        if not any(c.get_id() == course_id for c in self.courses):
            print("Không tìm thấy môn học.")
            return

        if course_id not in self.marks:
            self.marks[course_id] = {}

        for student in self.students:
            mark = float(input(f"Nhập điểm cho {student.get_name()} (ID: {student.get_id()}): "))
            self.marks[course_id][student.get_id()] = mark

    def show_marks(self):
        print("\n--- BẢNG ĐIỂM ---")
        self.list_courses()
        course_id = input("Chọn ID môn học để xem điểm: ")
        
        if course_id in self.marks:
            print(f"Điểm môn {course_id}:")
            for student in self.students:
                s_id = student.get_id()
                if s_id in self.marks[course_id]:
                    print(f"- {student.get_name()}: {self.marks[course_id][s_id]}")
                else:
                    print(f"- {student.get_name()}: Chưa có điểm")
        else:
            print("Chưa có điểm cho môn này.")

if __name__ == "__main__":
    sm = SchoolManagement()
    while True:
        print("\n=== QUẢN LÝ ĐIỂM (FULL OOP: PRIVATE & GET/SET) ===")
        print("1. Nhập sinh viên")
        print("2. Nhập môn học")
        print("3. Nhập điểm")
        print("4. DS Sinh viên")
        print("5. DS Môn học")
        print("6. Xem điểm")
        print("0. Thoát")
        
        choice = input("Chọn: ")
        if choice == '1': sm.input_students()
        elif choice == '2': sm.input_courses()
        elif choice == '3': sm.input_marks()
        elif choice == '4': sm.list_students()
        elif choice == '5': sm.list_courses()
        elif choice == '6': sm.show_marks()
        elif choice == '0': break
