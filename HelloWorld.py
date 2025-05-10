import random

# Define lists of sample first and last names of workers
first_names = [
    "John", "Jane", "Alex", "Emily", "Chris", "Katie", "Michael", 
    "Sarah", "David", "Laura", "Peter", "Linda", "James", "Jessica", 
    "Robert", "Mary", "William", "Patricia", "Daniel", "Elizabeth"
]
last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", 
    "Davis", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", 
    "Anderson", "Thomas", "Taylor", "Moore", "Jackson"
]

def generate_workers(num_workers=500):
    """Generate a list of workers with random names."""
    return [f"{random.choice(first_names)} {random.choice(last_names)}" for _ in range(num_workers)]

def determine_employee_level(worker, salary):
    """Determine the employee level based on salary and name."""
    female_names = ["Jane", "Emily", "Katie", "Sarah", "Laura", "Linda", "Jessica", "Mary", "Elizabeth"]
    
    if 10000 < salary < 20000:
        return "A1"
    elif 7500 < salary < 30000 and worker.split()[0] in female_names:
        return "A5-F"
    else:
        return "Unknown"

def generate_payslips(workers):
    """Generate and print payslips for each worker."""
    for worker in workers:
        salary = random.randint(7500, 30000)  # Random salary between 7,500 and 30,000
        employee_level = determine_employee_level(worker, salary)
        print(f"Payslip for {worker}: Salary = ${salary}, Employee Level = {employee_level}")

if __name__ == "__main__":
    random.seed(42)  # Optional: Set a seed for reproducibility
    workers = generate_workers()
    generate_payslips(workers)
