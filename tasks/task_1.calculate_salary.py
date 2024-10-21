from typing import Tuple

def total_salary(path: str) -> Tuple[int, float]:
    try:
        with open(path, 'r', encoding='utf-8') as employers_data_file:
            total_salary = 0
            count = 0

            for employer in employers_data_file:
                try:
                    name, salary = employer.rsplit(',', 1)
                    salary = int(salary)
                    total_salary += salary
                    count += 1
                except ValueError:
                    print(f"Wrong data format: {employer}.")
                    return 0, 0
            
            if count == 0:
                return 0, 0

            average_salary = total_salary / count

            return total_salary, average_salary

    except FileNotFoundError:
        print("File is not found.")
        return 0, 0
    
total, average = total_salary("tasks/test_data/salary_report.txt")
print(f"Total salary: {total}, avarage: {average}")
