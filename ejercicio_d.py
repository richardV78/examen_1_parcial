def validate_underage(age: int):
    return age < 18

print(
    "This person is underage"
    if validate_underage(int(input("Enter age: "))) else
    "This person is not underage"
)
