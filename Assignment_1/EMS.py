employees = {
    101: {
        'name': 'Satya',
        'age': 27,
        'department': 'HR',
        'salary': 50000
    }
}

def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    
    if emp_id in employees:
        print("Employee ID already exists. Please enter a new ID.")
        return
        
    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    department = input("Enter Employee Department: ")
    salary = int(input("Enter Employee Salary: "))
    
    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }
    
    print("Employee successfully added.")

def view_employees():
    if not employees:
        print("No employees available.")
        return
        
    print(f"{'ID':<10} | {'Name':<15} | {'Age':<5} | {'Department':<15} | {'Salary':<10}")
    print("-" * 65)
    
    for emp_id, details in employees.items():
        print(f"{emp_id:<10} | {details['name']:<15} | {details['age']:<5} | {details['department']:<15} | {details['salary']:<10}")

def search_employee():
    emp_id = int(input("Enter the Employee ID you want to search for: "))
    
    if emp_id in employees:
        details = employees[emp_id]
        print(f"Name: {details['name']}")
        print(f"Age: {details['age']}")
        print(f"Department: {details['department']}")
        print(f"Salary: {details['salary']}")
    else:
        print("Employee not found.")

def main_menu():
    while True:
        print("\nEmployee Management System (EMS)")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            print("Thank you! Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
