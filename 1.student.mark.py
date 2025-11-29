
students = [] 
courses = [] 
marks = {}    
def input_number_of_students():
    count = int(input("Nhập số lượng sinh viên trong lớp: "))
    return count

def input_student_information():
    print("\n--- NHẬP THÔNG TIN SINH VIÊN ---")
    id = input("Nhập ID sinh viên: ")
    name = input("Nhập tên sinh viên: ")
    dob = input("Nhập ngày sinh (dd/mm/yyyy): ")
    student = {'id': id, 'name': name, 'dob': dob}
    students.append(student)

def input_number_of_courses():
    count = int(input("\nNhập số lượng môn học: "))
    return count

def input_course_information():
    print("\n--- NHẬP THÔNG TIN MÔN HỌC ---")
    id = input("Nhập ID môn học: ")
    name = input("Nhập tên môn học: ")
    
    course = {'id': id, 'name': name}
    courses.append(course)

def input_marks():
    print("\n--- NHẬP ĐIỂM ---")
    if len(courses) == 0:
        print("Chưa có môn học nào!")
        return
    
    list_courses()
    course_id = input("Chọn ID môn học để nhập điểm: ")
    course_exists = False
    for course in courses:
        if course['id'] == course_id:
            course_exists = True
            break
    
    if not course_exists:
        print("Môn học không tồn tại.")
        return
    if course_id not in marks:
        marks[course_id] = {}
    for student in students:
        mark = float(input(f"Nhập điểm cho sinh viên {student['name']} (ID: {student['id']}): "))
        marks[course_id][student['id']] = mark

def list_students():
    print("\n--- DANH SÁCH SINH VIÊN ---")
    if len(students) == 0:
        print("Chưa có sinh viên nào.")
    else:
        for s in students:
            print(f"ID: {s['id']}, Tên: {s['name']}, Ngày sinh: {s['dob']}")

def list_courses():
    print("\n--- DANH SÁCH MÔN HỌC ---")
    if len(courses) == 0:
        print("Chưa có môn học nào.")
    else:
        for c in courses:
            print(f"ID: {c['id']}, Tên: {c['name']}")

def show_marks():
    print("\n--- BẢNG ĐIỂM ---")
    list_courses()
    course_id = input("Nhập ID môn học muốn xem điểm: ")
    
    if course_id in marks:
        print(f"Điểm môn {course_id}:")
        for student in students:
            s_id = student['id']
            if s_id in marks[course_id]:
                print(f"Sinh viên {student['name']} (ID: {s_id}): {marks[course_id][s_id]}")
            else:
                print(f"Sinh viên {student['name']} (ID: {s_id}): Chưa có điểm")
    else:
        print("Chưa có điểm cho môn học này hoặc ID sai.")


def main():
    while True:
        print("\n==============================")
        print("HỆ THỐNG QUẢN LÝ ĐIỂM SINH VIÊN")
        print("1. Nhập số lượng sinh viên")
        print("2. Nhập thông tin sinh viên")
        print("3. Nhập số lượng môn học")
        print("4. Nhập thông tin môn học")
        print("5. Nhập điểm cho môn học")
        print("6. Xem danh sách sinh viên")
        print("7. Xem danh sách môn học")
        print("8. Xem điểm thi")
        print("0. Thoát")
        
        choice = input("Chọn chức năng (0-8): ")
        
        if choice == '1':
            num = input_number_of_students()
            print(f"Đã ghi nhận số lượng: {num}") 
        elif choice == '2':
            input_student_information()
        elif choice == '3':
            num = input_number_of_courses()
        elif choice == '4':
            input_course_information()
        elif choice == '5':
            input_marks()
        elif choice == '6':
            list_students()
        elif choice == '7':
            list_courses()
        elif choice == '8':
            show_marks()
        elif choice == '0':
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()