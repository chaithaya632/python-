library_members = {
    101: "Rahul",
    102: "Anita",
    103: "Suresh"
}

print("---- Library Management System ----")

roll_input = input("Enter Roll Number: ")

 
if roll_input.isdigit():
    roll_no = int(roll_input)
    name = input("Enter Name: ")

    found = False

    for r_no in library_members:
        if r_no == roll_no:
            print("Member already exists.")
            print(f"Roll Number: {r_no}")
            print(f"Name: {library_members[r_no]}")
            found = True
            break

    if not found:
        print("New member detected. Registering...")
        library_members[roll_no] = name
        print("Registration successful.")

    print("\nUpdated Member List:")
    print(library_members)

else:
    print("Invalid roll number. Enter numbers only.")
