def validate_underage(age: int):
    return age < 18

def main():
    print(
        "This person is underage"
        if validate_underage(int(input("Enter age: "))) else
        "This person is not underage"
    )

if __name__ == "__main__":
    main()
