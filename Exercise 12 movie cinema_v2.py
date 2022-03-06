"""Keep track of ticket sales at a cinema
Version 2 - includes integer checker and error control on ticket choice
"""


# This function runs the main program and coordinates calls to other functions
def main_routine():
    adult_tickets = 0
    student_tickets = 0
    child_tickets = 0
    gift_tickets = 0
    total_sales = 0
    tickets_sold = 0

    ticket_wanted = input("Do you want to sell a ticket? (Y/N): ").upper()
    while ticket_wanted != "N":
        ticket = sell_ticket()
        print(ticket)

        # get the number of tickets wanted in the category chosen
        # includes check for valid integer
        num_tickets = integer_checker("How many of these tickets do you want: ")
        confirm = input(f"Confirm purchase of {num_tickets} type {ticket} "
                        f"ticket(s)? (Y/N): ").upper()
        if confirm == "Y":  # Giving user the option to cancel the sale
            price = num_tickets * float(get_price(ticket))
            total_sales += price
            tickets_sold += num_tickets
            if ticket == "A":
                adult_tickets += num_tickets
            elif ticket == "C":
                student_tickets += num_tickets
            elif ticket == "S":
                child_tickets += num_tickets
            else:
                gift_tickets += num_tickets

            ticket_wanted = input("\nDo you want to sell "
                                  "another ticket? (Y/N): ").upper()

    print("==================================================")
    print(f"The total tickets sold today was {tickets_sold}\n"
          f"This was made up of: \n"
          f"\t{adult_tickets} for adults; and \n"
          f"\t{student_tickets} for students; and \n"
          f"\t{child_tickets} for children; and \n"
          f"\t{gift_tickets} gift vouchers \n")
    print(f"Sales for the day came to ${total_sales:.2f}")
    print("==================================================")


# Get the category of ticket the purchaser wants
# Includes error control to ensure valid input
def sell_ticket():
    ticket_type_ = ""
    valid_choice = ["A", "S", "C", "G"]
    while ticket_type_ not in valid_choice:
        ticket_type_ = input("What kind of ticket do you want: \n"
                             "\tA for Adult, or\n"
                             "\tS for Student, or\n"
                             "\tC for Child, or \n"
                             "\tG for Gift voucher\n"
                             ">> ").upper()  # uppercase to minimise input errors
        if ticket_type_ not in valid_choice:
            print("Sorry, please choose one of the options")
        else:
            return ticket_type_


# Get the price for each ticket in the category of ticket chosen
def get_price(type_):
    prices = [["A", 12.5], ["S", 9], ["C", 7], ["G", 0]]
    for price in prices:
        if price[0] == type_:
            return price[1]


# Integer checking function - loops until a valid number is entered
def integer_checker(question):
    error = "\nSorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


# Main routine
print("**************** Fanfare Movies - ticketing system ****************\n")
main_routine()




