# Simple Money Withdrawal System with Error Handling

balance = 5000.00  # Starting balance

while True:
    try:
        print("\n=== MONEY WITHDRAWAL SYSTEM ===")
        print("Current Balance: ₱", balance)

        withdraw = float(input("Enter amount to withdraw: ₱"))

        # Check if withdrawal is valid
        if withdraw <= balance:
            balance -= withdraw
            print("Withdrawal successful!")
            print("Remaining balance: ₱", balance)

        else:
            print("Insufficient funds!")

            # Options after error
            while True:
                print("\nChoose an option:")
                print("1 - Try again")
                print("2 - Check balance")
                print("3 - Exit")

                choice = input("Enter choice: ")

                if choice == "1":
                    break  # Go back to withdrawal

                elif choice == "2":
                    print("Your current balance is: ₱", balance)

                elif choice == "3":
                    print("Thank you for using the system.")
                    exit()

                else:
                    print("Invalid choice. Try again.")

    except ValueError:
        print("Invalid input! Please enter a valid number.")