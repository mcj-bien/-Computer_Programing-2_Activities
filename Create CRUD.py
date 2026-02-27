# Create CRUD system (Create, Read, Update, Delete)

users = []  

while True:
    print("\n--- User Management System ---")
    print("1. Show Users")
    print("2. Add Users")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        if users:
            print("\nUser List:")
            for i, user in enumerate(users, start=1):
                print(f"{i}. {user}")
        else:
            print("\nNo users found.")
            
    elif choice == '2':
        new_user = input("Enter new user name: ")
        users.append(new_user)
        print(f"User {new_user} added successfully.")
        
    elif choice == '3':
        if users:
            for i, user in enumerate(users, start=1):
                print(f"{i}. {user}")
            try:
                index = int(input("Enter the number of user to update: ")) - 1
                if 0 <= index < len(users):
                    updated_user = input("Enter the new name: ")
                    print(f"User {users[index]} updated to {updated_user}.")
                    users[index] = updated_user
                else:
                    print("Invalid user number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No users to update.")
            
    elif choice == '4':
        if users:
            for i, user in enumerate(users, start=1):
                print(f"{i}. {user}")
            try:
                index = int(input("Enter the number of the user to delete: ")) - 1
                if 0 <= index < len(users):
                    removed_user = users.pop(index)
                    print(f"User {removed_user} deleted successfully.")
                else:
                    print("Invalid user number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No users to delete.")
            
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")