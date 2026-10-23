import database
import student


def main():
    connected, message = database.test_connection()
    if not connected:
        print(f"Cant connect to XAMPP MySQL: {message}")
        print("Make sure MySQL is running and the schema.sql is imported.")
        return
    print(message)

    print("\n=== STUDENT ADDING SYSTEM ===")
    while True:
        print("\n[1] Add Student")
        print("[2] View all students")
        print("[3] Search student")
        print("[4] Edit the student information ")
        print("[5] Delete student")
        print("[6] Delete all students")
        print("[0] You can exit the program.")
        choice = input("Piliin: ").strip()

        if choice == "1":
            student.add_student()
        elif choice == "2":
            student.show_students()
        elif choice == "3":
            student.search_student()
        elif choice == "4":
            student.edit_student()
        elif choice == "5":
            student.remove_student()
        elif choice == "6":
            student.remove_all_students()
        elif choice == "0":
            print("Thank u for using the program. byyyyeerrrss")
            break
        else:
            print("Invalid choice. Please .")


if __name__ == "__main__":
    main()
