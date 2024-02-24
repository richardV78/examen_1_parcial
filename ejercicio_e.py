def validate_tuition_discount(grade: int):
    return grade > 95

def main():
    print(
        "You will receive a tuition discount (Grade is over 95%)"
        if validate_tuition_discount(int(input("Enter the student's grade: "))) else
        "You will not receive a tuition discount (Grade is less than 95%)"
    )


if __name__ == "__main__":
    main()
