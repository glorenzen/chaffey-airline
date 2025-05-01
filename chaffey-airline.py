# This app is a simple point of sale system for Chaffey College's new Airline.

# Initialize the flight classes
OPEN = "Open"
# First class has 4 rows and 2 seats per row
first_class = [[OPEN] * 2 for _ in range(4)]
# Coach class has 10 rows and 4 seats per row
coach_class = [[OPEN] * 4 for _ in range(10)]


def display_options():
    available_first_class = sum(row.count(OPEN) for row in first_class)
    available_coach_class = sum(row.count(OPEN) for row in coach_class)
    print("1) Make a new first class reservation")
    print(f"   a. Only {available_first_class} seats are available at $500")
    print("2) Make a new coach class reservation")
    print(f"   a. Only {available_coach_class} seats are available at $199")
    print("3) Change an existing reservation")
    print("4) Print the listing of seats")
    print("5) Quit")


def print_seat_chart():
    print("First Class Seat Chart:")
    print("          A              B")
    for i, row in enumerate(first_class):
        print(f"{i:<3} " + " | ".join(f"{seat[:12]:^12}" for seat in row))
    print("\nCoach Class Seat Chart:")
    print("          A              B              C              D")
    for i, row in enumerate(coach_class):
        print(f"{i:<3} " + " | ".join(f"{seat[:12]:^12}" for seat in row))
    print("=" * 83)

    if all(OPEN not in row for row in first_class):
        print("No first class seats are open.")
    if all(OPEN not in row for row in coach_class):
        print("No coach class seats are open.")


def calculate_cost(seat_class, age):
    tax = 0.09
    discount = 0.20 if age < 7 or age >= 65 else 0

    if seat_class == first_class:
        return (500 - 500 * discount) + (500 * tax)
    else:
        return (199 - 199 * discount) + (199 * tax)


def print_denominations(change):
    denominations = [100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]

    for denomination in denominations:
        count = int(change // denomination)
        name = ""
        # Get the name of the denomination if less than 1
        if denomination < 1:
            names = {0.25: "Quarter", 0.10: "Dime", 0.05: "Nickel", 0.01: "Penny"}
            name = names.get(denomination, f"${denomination:.2f}")
        else:
            name = f"${denomination:.2f}"

        if count > 0:
            print(f"{name} x {count}")
            change -= count * denomination
        else:
            print(f"{name} x 0")


def is_valid_row_selection(seat_class: list, row: int):
    if (
        row < 0
        or (row > 3 and seat_class == first_class)
        or (row > 9 and seat_class == coach_class)
    ):

        return False
    return True


def is_valid_seat_selection(seat_class: list, seat_index: int):

    if seat_class == first_class:
        if seat_index < 0 or seat_index > 1:
            return False
    else:
        if seat_index < 0 or seat_index > 3:
            return False

    return True


def make_reservation(seat_class):
    print("Please enter the row number (0-3 for first class, 0-9 for coach class):")

    row = int(input("Row: "))
    if not is_valid_row_selection(seat_class, row):
        print("Invalid row number. Please try again.")
        return

    seat_letter = input("Seat: ")
    seat_index = ord(seat_letter.upper()) - ord("A")
    if not is_valid_seat_selection(seat_class, seat_index):
        print("Invalid seat letter. Please try again.")
        return

    if seat_class[row][seat_index] == OPEN:
        name = input("Please enter your name: ")
        seat_class[row][seat_index] = name
        age = int(input("Please enter your age: "))
        cost = calculate_cost(seat_class, age)
        amount_given = int(input(f"Cost is ${cost:.2f}. Please enter amount given: "))
        change = amount_given - cost
        print(f"Reservation made for {name} in seat {row} {chr(65 + seat_index)}.")
        print(f"Change: ${change:.2f}")
        print_denominations(change)
    else:
        print("Sorry, that seat is already reserved.")


def change_reservation(seat_class):
    print("Please enter the row number (0-3 for first class, 0-9 for coach class):")

    row = int(input("Row: "))
    if not is_valid_row_selection(seat_class, row):
        print("Invalid row number. Please try again.")
        return

    seat_letter = input("Seat: ")
    seat_index = ord(seat_letter.upper()) - ord("A")
    if not is_valid_seat_selection(seat_class, seat_index):
        print("Invalid seat letter. Please try again.")
        return

    if seat_class[row][seat_index] != OPEN:
        print(
            f"Seat {row} {chr(65 + seat_index)} is currently reserved by {seat_class[row][seat_index]}."
        )
        seat_class[row][seat_index] = OPEN
        print(f"Seat {row} {chr(65 + seat_index)} is now open.")
        print("Please choose a new seat class: ")
        print("1) First Class")
        print("2) Coach Class")
        class_choice = input("Please enter your choice (1-2): ")
        if class_choice == "1":
            seat_class = first_class
        elif class_choice == "2":
            seat_class = coach_class
        print("Please choose a new seat.")
        make_reservation(seat_class)
    else:
        print("Sorry, that seat is not reserved.")


def main():
    print("=" * 83)
    print(
        "========================== Welcome to Chaffey Airlines ============================"
    )
    print("=" * 83)
    print("What would you like to do?")

    while True:
        display_options()
        choice = input("Please enter your choice (1-5): ")

        if choice == "1":
            print("You have chosen to make a new first class reservation.")
            make_reservation(first_class)
        elif choice == "2":
            print("You have chosen to make a new coach class reservation.")
            make_reservation(coach_class)
        elif choice == "3":
            print("You have chosen to change an existing reservation.")
            print("Please choose a class:")
            print("1) First Class")
            print("2) Coach Class")
            class_choice = input("Please enter your choice (1-2): ")
            if class_choice == "1":
                change_reservation(first_class)
            elif class_choice == "2":
                change_reservation(coach_class)
            else:
                print("Invalid choice. Please enter 1 or 2.")
        elif choice == "4":
            print("You have chosen to print the listing of seats.")
            print_seat_chart()
        elif choice == "5":
            print("Thank you for using Chaffey Airlines. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
        print("=" * 83)


if __name__ == "__main__":
    main()
