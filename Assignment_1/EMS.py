import json
import random
import os

# --- STEP 1: DEFINE CLASSES AND FUNCTIONS FIRST ---

class EMS:
    company_name = "Tutedude"
    description = "Employee Management System"
    
    def __init__(self, empid, name, age, department, salary):
        self.empid = empid
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary
        
    def emp_data_store(self):
        """Converts the object data into a python dictionary."""
        return {
            str(self.empid): {
                "name": self.name,
                "age": self.age,
                "department": self.department,
                "salary": self.salary
            }
        }
    
    def store_data(self):
        """Saves data by APPENDING to the JSON file inside Assignment_1 folder."""
        # POINT TO THE UPDATED FILE PATH VARIABLE
        existing_data = _load_raw_data(FILE_PATH)

        # Merge the new employee data into our database
        new_data = self.emp_data_store()
        existing_data.update(new_data)

        # Write everything back to the file using our internal save rules
        _save_raw_data(FILE_PATH, existing_data)
        print(f"Success: Employee '{self.name}' was successfully added with ID: {self.empid}")

# --- PROTECTED FILE METHODS ---

def _load_raw_data(file_path):
    """Protected Helper: Safely reads records from the specific file path."""
    # EXTRACT THE FOLDER PATH AND AUTO-CREATE IT IF IT IS MISSING
    folder_path = os.path.dirname(file_path)
    if folder_path:
        os.makedirs(folder_path, exist_ok=True)

    # Step 1 - Initialize the file with sample data if it does not exist
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        sample_data = {
            "101": {
                "name": "Satya",
                "age": 27,
                "department": "HR",
                "salary": 50000
            }
        }
        _save_raw_data(file_path, sample_data)
        return sample_data

    with open(file_path, "r") as json_file:
        try:
            return json.load(json_file)
        except json.JSONDecodeError:
            return {}

def _save_raw_data(file_path, data):
    """Protected Helper: Writes a raw dictionary straight to the file path."""
    # DOUBLE-CHECK FOLDER CREATION BEFORE WRITING
    folder_path = os.path.dirname(file_path)
    if folder_path:
        os.makedirs(folder_path, exist_ok=True)

    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)

def _generate_unique_id(current_db):
    """Protected Helper: Automatically generates and verifies a unique ID."""
    while True:
        generated_id = random.randint(1000, 9999)
        if str(generated_id) not in current_db:
            return generated_id


# --- STEP 2: APP RUNNER BLOCK ---

if __name__ == "__main__":
    # DEFINE THE SUBFOLDER PATH HERE USING OS.PATH.JOIN FOR SYSTEM COMPATIBILITY
    FILE_PATH = os.path.join("Assignment_1", "EMS_Data.json")
    
    # Step 2 - Implement a loop to continuously display the menu until Exit
    while True:
        print("\n*** Employee Management System (EMS) ***")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        
        question_1 = input("Select an option (1-4): ")
        
        # Step 3 - Add Employee Functionality
        if question_1 == "1":
            current_db = _load_raw_data(FILE_PATH)
            
            # Auto-generate and verify the unique Employee ID
            new_id = _generate_unique_id(current_db)
            print(f"\n[System] Auto-Generated & Verified Unique ID: {new_id}")
            
            # 1. Prompt the User to enter employee details
            name = input("Enter Employee Name: ")
            age = int(input("Enter Employee Age: "))
            department = input("Enter Employee Department: ")
            salary = int(input("Enter Employee Salary: "))
            
            # Instantiate object and store data to dictionary/file
            emp1 = EMS(new_id, name, age, department, salary)
            emp1.store_data()
            
        # Step 4 - View All Employees
        elif question_1 == "2":
            current_db = _load_raw_data(FILE_PATH)
            
            if not current_db:
                print("No employees available.")
            else:
                print(f"\n{'ID':<8}{'Name':<15}{'Age':<8}{'Department':<15}{'Salary':<10}")
                print("-" * 56)
                for emp_id, details in current_db.items():
                    print(f"{emp_id:<8}{details['name']:<15}{details['age']:<8}{details['department']:<15}{details['salary']:<10}")
                    
        # Step 5 - Search for an Employee by ID
        elif question_1 == "3":
            current_db = _load_raw_data(FILE_PATH)
            
            search_id = input("Enter the Employee ID to search for: ")
            
            if search_id in current_db:
                emp = current_db[search_id]
                print(f"\nEmployee Found:")
                print(f"Name: {emp['name']}")
                print(f"Age: {emp['age']}")
                print(f"Department: {emp['department']}")
                print(f"Salary: {emp['salary']}")
            else:
                print("Employee not found.")
                
        # Step 6 - Exit the Program
        elif question_1 == "4":
            print("\nThank you for using the Employee Management System. Goodbye!")
            break
            
        else:
            print("\nInvalid choice! Please select a valid number from 1 to 4.")
