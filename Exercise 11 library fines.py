# Calculate overdue fines for books at a library
def calc_fines(days_overdue):
    fine = .5 + (days_overdue * .8)
    if fine > 30:
        fine = 30
    return fine


# Main routine
days_overdue_ = int(input("Enter days overdue: "))
print(f"For {days_overdue_} the fine is ${calc_fines(days_overdue_):.2f}")

