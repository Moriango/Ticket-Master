TICKET_COST = 10
total_tickets = 100

def printTickets(ticket):
    print("There are {} ticket(s) remaining".format(total_tickets))

while total_tickets:
    printTickets(total_tickets)
    name = input("What is your name? ")

    num_tickets = input("Hello {}, how many tickets would you like? ".format(name))
    try: 
        num_tickets = int(num_tickets)
        if num_tickets > total_tickets:
            raise ValueError("Sorry {}, we don't have that many tickets left :'(".format(name))
    except ValueError as err:
        print("There seems to be an issue. \n{} \nPlease try again".format(err))
    else: 
        amount_due = int(num_tickets) * TICKET_COST + 2
        print("Since you ordered {} ticket(s), with a two dollar service charge. \nYour total amount due is {} dollars".format(num_tickets, amount_due))
        proceed = input("Would you like to continue your order, {} ".format(name))
        if proceed.lower() in {'yes', 'yeah', 'y', 'yup'}:
            print("SOLD{}".format("!"*num_tickets))
            total_tickets -= num_tickets
        else: 
            print("Thank you anyways, {}!".format(name))