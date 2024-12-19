students = {}

while True:
    print("\nStudent Records Management System")
    print("1. Add Student Record")
    print("2. Update Student Record")
    print("3. Delete Student Record")
    print("4. Display All Records with Analysis")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        student_id = input("Enter Student ID: ")
        if student_id in students:
            print("Student ID already exists!")
        else:
            name = input("Enter Student Name: ")
            subjects = {}
            while True:
                subject = input("Enter subject name (or type 'done' to finish): ")
                if subject.lower() == "done":
                    break
                marks = int(input(f"Enter marks for {subject}: "))
                subjects[subject] = marks
            students[student_id] = {"name": name, "subjects": subjects}
            print("Student record added successfully!")

    elif choice == "2":
        student_id = input("Enter Student ID to update: ")
        if student_id not in students:
            print("Student ID not found!")
        else:
            print("1. Update Name")
            print("2. Update Marks")
            update_choice = input("Enter your choice (1-2): ")
            if update_choice == "1":
                new_name = input("Enter new name: ")
                students[student_id]["name"] = new_name
                print("Name updated successfully!")
            elif update_choice == "2":
                subject = input("Enter subject name to update marks: ")
                if subject in students[student_id]["subjects"]:
                    new_marks = int(input(f"Enter new marks for {subject}: "))
                    students[student_id]["subjects"][subject] = new_marks
                    print("Marks updated successfully!")
                else:
                    print("Subject not found!")

    elif choice == "3":
        student_id = input("Enter Student ID to delete: ")
        if student_id in students:
            del students[student_id]
            print("Student record deleted successfully!")
        else:
            print("Student ID not found!")

    elif choice == "4":
        if not students:
            print("No student records available.")
        else:
            print("\nStudent Records:")
            results = []
            for student_id, data in students.items():
                total_marks = sum(data["subjects"].values())
                percentage = total_marks / len(data["subjects"]) if data["subjects"] else 0
                results.append((total_marks, percentage, student_id, data["name"]))

            results.sort(reverse=True, key=lambda x: x[0])

            for rank, (total_marks, percentage, student_id, name) in enumerate(results, start=1):
                print(f"Rank {rank}: {name} (ID: {student_id})")
                print(f"  Total Marks: {total_marks}")
                print(f"  Percentage: {percentage:.2f}%")

    elif choice == "5":
        
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
