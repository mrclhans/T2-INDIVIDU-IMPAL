
students = []

def add_student():
    name = input("Masukan Nama Mahasiswa: ")
    nim = input("Masukan NIM Mahasiswa: ")
    department = input("Masukan Program Studi Mahasiswa: ")
    year = input("Tahun masuk: ")
    
    for student in students:
        if student['NIM'] == nim:
            print("Error: NIM sudah digunakan!")
            return
    
    students.append({
        'name': name,
        'NIM': nim,
        'department': department,
        'year': year
    })
    print("Mahasiswa Berhasil ditambahkan!")

def view_students():
    if len(students) == 0:
        print("Mahasiswa tidak ditemukan")
    else:
        for student in students:
            print(f"Name: {student['name']}, NIM: {student['NIM']}, Department: {student['department']}, Year: {student['year']}")

def edit_student():
    nim = input("Masukan NIM Mahasiswa untuk di edit: ")
    for student in students:
        if student['NIM'] == nim:
            student['name'] = input("Masukan Nama Baru: ")
            student['department'] = input("Masukan Program Studi Baru: ")
            student['year'] = input("Masukan Tahun Masuk Baru: ")
            print("Data Mahasiswa Berhasil Diperbarui")
            return
    print("Error: Mahasiswa tidak ditemukan!")

def delete_student():
    nim = input("Masukan NIM Mahasiswa untuk dihapus: ")
    for student in students:
        if student['NIM'] == nim:
            students.remove(student)
            print("Mahasiswa Berhasil dihapus!")
            return
    print("Error: Mahasiswa tidak ditemukan")

def menu():
    while True:
        print("\nManajemen Mahasiswa - Fakultas Informatika")
        print("1. Tambahkan Mahasiswa")
        print("2. Lihat Mahasiswa")
        print("3. Edit Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Keluar")
        choice = input("Pilih opsi: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            edit_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            break
        else:
            print("Opsi salah, silahkan pilih opsi yang benar")


menu()
