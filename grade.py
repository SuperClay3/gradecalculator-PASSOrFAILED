def get_grade_status(grade):
    return "Passed" if grade >= 75 else "Failed"


def main():
    while True:
        try:
            num_subjects = int(input("Enter the number of subjects: "))
            if num_subjects <= 0:
                print("Invalid input. Number of subjects must be positive.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for the number of subjects.")

    total_grade = 0

    for i in range(1, num_subjects + 1):
        subject = f"Subject {i}"

        while True:
            try:
                grade = float(input(f"Enter the grade for {subject}: "))
                if grade < 0 or grade > 100:
                    print("Invalid input. Grade must be between 0 and 100.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the grade.")

        status = get_grade_status(grade)
        total_grade += grade
        print(f"{subject}: {grade} - {status}")

    average_grade = total_grade / num_subjects
    average_status = get_grade_status(average_grade)

    print("\nTotal Average Grade: {:.2f} - {}".format(average_grade, average_status))


if __name__ == "__main__":
    main()

