def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0
            
            for line in file:
                # Check if the line is not empty
                if line.strip():
                    # Split the line into name and salary
                    _, salary = line.split(',')
                    total += int(salary)
                    count += 1
            
            # Calculate the average salary
            average = total / count if count > 0 else 0
            
            return total, average

    except FileNotFoundError:
        print("Error: File not found.")
        return 0, 0
    except Exception as e:
        print(f"Error: {e}")
        return 0, 0
    
# Path to the sample data file
path = "task1/sample_salaries.txt"

# Call the function with the path to the data file
total, average = total_salary(path)

# Print the results
print(f"Total salary: {total}, Average salary: {average}")