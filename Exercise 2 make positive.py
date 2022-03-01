# Function to get the absolute value of a number
def make_positive(number):
    new_value = abs(number)
    return new_value


# Main routine
number_to_check = int(input("Enter a number: "))
print(f"The absolute value of {number_to_check} is "
      f"{make_positive(number_to_check)}")

