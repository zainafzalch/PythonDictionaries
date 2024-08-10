# 2. Python Programming Challenges for Customer Service Data Handling

# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Problem Statement: Develop a program that:

#     Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).

#     Implement functions to:

#         Open a new service ticket.

#         Update the status of an existing ticket.

#         Display all tickets or filter by status.

#     Initialize with some sample tickets and include functionality for additional ticket entry.

# Example ticket structure:

# service_tickets = {
#     "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
#     "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
# }

service_tickets = {
    "Ticket-1": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket-2": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(service_tickets):
    ticket = "Ticket-" + str(len(service_tickets)+1)
    customer = input("Enter Customer Name: ").capitalize()
    issue = input("Enter Issue Description: ").capitalize()
    status = "open"
    service_tickets[ticket] = {"Customer":customer, "Issue":issue,"Status":status}
    return service_tickets

def display_all(service_tickets):
    filter_or_not = input("Would you like to filter by status? (y/n) ")

    if filter_or_not == "y":
        status = input("Enter Status to Filter By (open/closed): ").lower()
        if status not in ["open","closed"]:
            print("Invalid Status. Please try again.")
            display_all(service_tickets)

        elif status == "closed":
            for tickets, ticket_details in service_tickets.items():
                if ticket_details["Status"] == "closed":
                    print(f"{tickets} : {ticket_details}")
                
        else:
            for tickets, ticket_details in service_tickets.items():
                if ticket_details["Status"] == "open":
                    print(f"{tickets} : {ticket_details}")

    elif filter_or_not not in ["y","n"]:
        print("Invalid Filer option. Please try again.")
        display_all(service_tickets)

    else:
        for key in service_tickets.keys():
            print(key,":",service_tickets[key])

def update_ticket(service_tickets):
    display_all(service_tickets)
    ticket = input("Enter Ticket ID to Update Status: ").capitalize()
    service_tickets[ticket]["Status"] = "closed"
    return service_tickets

def main():
    while True:
        menu = """
        1. Open a new ticket
        2. Display All Tickets
        3. Update Ticket Status
        4. Exit
        """
        print(menu)

        try:
            choice = int(input("Enter Choice: "))
            if choice > 4:
                print("Invalid Choice")
                main()
        except ValueError as e:
            print("Invalid Choice")
            main()
        else:
            match choice:
                case 1:
                    open_ticket(service_tickets)
                    main()
                case 2:
                    display_all(service_tickets)
                    main()
                case 3:
                    update_ticket(service_tickets)
                    main()
                case 4:
                    print("Thank You. Good bye!")
                    service_tickets.clear()
                    exit()
main()