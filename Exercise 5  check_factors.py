# Function to check if a number is a factor of a larger number
def check_factor(big_num, small_num):
    return big_num % small_num == 0


# Main routine
big = int(input("Enter the bigger number: "))
small = int(input("Enter the smaller number: "))
if check_factor(big, small):
    print(f"{small} is a factor of {big}")
else:
    print(f"{small} is NOT a factor of {big}")

