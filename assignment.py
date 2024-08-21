# Question 1.6. Write a program to display the appropriate message as per the color of signal (RED-Stop/Yellow-Stay/ Green-Go) at the road crossing.
signal = input("Enter the signal color (Red/Yellow/Green): ").lower()

if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Stay")
elif signal == "green":
    print("Go")
else:
    print("Invalid signal color")

# Question 1.7. Write a program to create a simple calculator performing only four basic operations(+,-./.*).
def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        print(f"Result: {num1 + num2}")
    elif operation == "-":
        print(f"Result: {num1 - num2}")
    elif operation == "*":
        print(f"Result: {num1 * num2}")
    elif operation == "/":
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed")
    else:
        print("Invalid operation")

calculator()

# Question 1.8. Write a program to find the larger of the three pre-specified numbers using ternary operators.
a, b, c = 10, 20, 15
largest = a if (a > b and a > c) else (b if b > c else c)
print(f"The largest number is: {largest}")

# Question 1.9. Write a program to find the factors of a whole number using a while loop.
num = int(input("Enter a number: "))
i = 1

print(f"Factors of {num} are:")
while i <= num:
    if num % i == 0:
        print(i)
    i += 1

# Question 1.10. Write a program to find the sum of all the positive numbers entered by the user. As soon as the user enters a negative number, stop taking in any further input from the user and display the sum.
total = 0

while True:
    num = int(input("Enter a number (negative number to stop): "))
    if num < 0:
        break
    total += num

print(f"The sum of all positive numbers is: {total}")

# Question 1.11. Write a program to find prime numbers between 2 to 100 using nested for loops.
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")

# Question 1.12. Write the programs for the following:
# Accept the marks of the student in five major subjects and display the same.
subjects = ["Math", "Science", "English", "History", "Geography"]
marks = []

for subject in subjects:
    mark = int(input(f"Enter marks for {subject}: "))
    marks.append(mark)

print("\nMarks Obtained:")
for subject, mark in zip(subjects, marks):
    print(f"{subject}: {mark}")

# Calculate the sum of the marks of all subjects. Divide the total marks by number of subjects (ie. 5), calculate percentage total marks/5 and display the percentage.
# Program to calculate sum, percentage, and grade
total_marks = sum(marks)
percentage = total_marks / len(subjects)

print(f"\nTotal Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")

# Determining grade using match-case
match percentage:
    case _ if percentage > 85:
        grade = "A"
    case _ if 75 <= percentage <= 85:
        grade = "B"
    case _ if 50 <= percentage < 75:
        grade = "C"
    case _ if 30 <= percentage < 50:
        grade = "D"
    case _:
        grade = "Reappear"

print(f"Grade: {grade}")

# Question 1.13. Write a program for VIBGYOR Spectrum based on their Wavelength using. 
wavelength = float(input("Enter the wavelength in nm: "))

if 400.0 <= wavelength < 440.0:
    color = "Violet"
elif 440.0 <= wavelength < 460.0:
    color = "Indigo"
elif 460.0 <= wavelength < 500.0:
    color = "Blue"
elif 500.0 <= wavelength < 570.0:
    color = "Green"
elif 570.0 <= wavelength < 590.0:
    color = "Yellow"
elif 590.0 <= wavelength < 620.0:
    color = "Orange"
elif 620.0 <= wavelength <= 720.0:
    color = "Red"
else:
    color = "Wavelength out of VIBGYOR range"

print(f"The color corresponding to {wavelength} nm is: {color}")

# Question 1.14. Consider the gravitational interactions between the Earth, Moon, and Sun in our solar system.
# Given data
mass_earth = 5.972e24  
mass_moon = 7.34767309e22  
mass_sun = 1.989e30  
distance_earth_sun = 1.496e11  
distance_moon_earth = 3.844e8  

# Gravitational constant
G = 6.674e-11  

# Calculate gravitational force between Earth and Sun
force_earth_sun = G * (mass_earth * mass_sun) / (distance_earth_sun ** 2)

# Calculate gravitational force between Moon and Earth
force_moon_earth = G * (mass_moon * mass_earth) / (distance_moon_earth ** 2)

# Display results
print(f"Gravitational force between Earth and Sun: {force_earth_sun:.2e} N")
print(f"Gravitational force between Moon and Earth: {force_moon_earth:.2e} N")

# Compare the forces
if force_earth_sun > force_moon_earth:
    print("\nThe gravitational force between Earth and Sun is stronger.")
else:
    print("\nThe gravitational force between Moon and Earth is stronger.")

# Explanation
print("\nExplanation:")
if force_earth_sun > force_moon_earth:
    print("The Earth is more attracted to the Sun than the Moon is to the Earth.")
else:
    print("The Moon is more attracted to the Earth than the Earth is to the Sun.")


# Question 6. Write a code for Restaurant Management System Using OOPS
class MenuItem:
    def __init__(self, name, description, price, category, _id):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.__id = _id 

    def update_item(self, name=None, description=None, price=None, category=None):
        if name: self.name = name
        if description: self.description = description
        if price: self.price = price
        if category: self.category = category

    def remove_item(self):
        del self

    def display_item(self):
        return f"Name: {self.name}, Description: {self.description}, Price: {self.price}, Category: {self.category}"


class FoodItem(MenuItem):
    def __init__(self, name, description, price, category, _id, cuisine_type):
        super().__init__(name, description, price, category, _id)
        self.cuisine_type = cuisine_type

    def display_item(self):
        return super().display_item() + f", Cuisine Type: {self.cuisine_type}"


class BeverageItem(MenuItem):
    def __init__(self, name, description, price, category, _id, size):
        super().__init__(name, description, price, category, _id)
        self.size = size

    def display_item(self):
        return super().display_item() + f", Size: {self.size}"

food = FoodItem("Burger", "Beef patty with cheese", 5.99, "Food", 101, "Fast Food")
beverage = BeverageItem("Coke", "Chilled soft drink", 1.99, "Beverage", 201, "500ml")

print(food.display_item())
print(beverage.display_item())

# Question 7.Write a code for Hotel Management System using OOPS
class Room:
    def __init__(self, room_number, room_type, rate, availability, _id):
        self.room_number = room_number
        self.room_type = room_type
        self.rate = rate
        self.__availability = availability 
        self.__id = _id  

    def book_room(self):
        if self.__availability:
            self.__availability = False
            return "Room booked successfully."
        else:
            return "Room is not available."

    def check_in(self):
        return "Guest checked in."

    def check_out(self):
        self.__availability = True
        return "Guest checked out."

    def display_room(self):
        return f"Room Number: {self.room_number}, Type: {self.room_type}, Rate: {self.rate}, Available: {self.__availability}"

class SuiteRoom(Room):
    def __init__(self, room_number, rate, availability, _id, amenities):
        super().__init__(room_number, "Suite", rate, availability, _id)
        self.amenities = amenities

    def display_room(self):
        return super().display_room() + f", Amenities: {self.amenities}"

class StandardRoom(Room):
    def __init__(self, room_number, rate, availability, _id, bed_type):
        super().__init__(room_number, "Standard", rate, availability, _id)
        self.bed_type = bed_type

    def display_room(self):
        return super().display_room() + f", Bed Type: {self.bed_type}"

suite = SuiteRoom(101, 250, True, 501, ["TV", "Wi-Fi", "Mini Bar"])
standard = StandardRoom(102, 100, True, 502, "Queen Size")

print(suite.display_room())
print(standard.display_room())

# Question 8. Write a code for Fitness Club Management System using OOPS
class Member:
    def __init__(self, name, age, membership_type, _id):
        self.name = name
        self.age = age
        self.membership_type = membership_type
        self.__status = "Active" 
        self.__id = _id 

    def renew_membership(self):
        self.__status = "Active"
        return "Membership renewed."

    def cancel_membership(self):
        self.__status = "Inactive"
        return "Membership cancelled."

    def display_member(self):
        return f"Name: {self.name}, Age: {self.age}, Membership Type: {self.membership_type}, Status: {self.__status}"

class FamilyMember(Member):
    def __init__(self, name, age, _id, family_size):
        super().__init__(name, age, "Family", _id)
        self.family_size = family_size

    def display_member(self):
        return super().display_member() + f", Family Size: {self.family_size}"

class IndividualMember(Member):
    def __init__(self, name, age, _id):
        super().__init__(name, age, "Individual", _id)

    def display_member(self):
        return super().display_member()

family_member = FamilyMember("John Doe", 40, 301, 4)
individual_member = IndividualMember("Jane Smith", 30, 302)

print(family_member.display_member())
print(individual_member.display_member())

# Question 9. Write a code for Event Management System using OOPS
class Event:
    def __init__(self, name, date, time, location, _id):
        self.name = name
        self.date = date
        self.time = time
        self.location = location
        self.__attendees = []  
        self.__id = _id  

    def add_attendee(self, attendee):
        self.__attendees.append(attendee)

    def remove_attendee(self, attendee):
        if attendee in self.__attendees:
            self.__attendees.remove(attendee)

    def total_attendees(self):
        return len(self.__attendees)

    def display_event(self):
        return f"Event: {self.name}, Date: {self.date}, Time: {self.time}, Location: {self.location}, Total Attendees: {self.total_attendees()}"

class PrivateEvent(Event):
    def __init__(self, name, date, time, location, _id, invitation_required):
        super().__init__(name, date, time, location, _id)
        self.invitation_required = invitation_required

    def display_event(self):
        return super().display_event() + f", Invitation Required: {self.invitation_required}"

class PublicEvent(Event):
    def __init__(self, name, date, time, location, _id, max_capacity):
        super().__init__(name, date, time, location, _id)
        self.max_capacity = max_capacity

    def display_event(self):
        return super().display_event() + f", Max Capacity: {self.max_capacity}"

private_event = PrivateEvent("Wedding", "2024-12-25", "18:00", "City Hall", 401, True)
public_event = PublicEvent("Concert", "2024-10-15", "20:00", "Central Park", 402, 500)

private_event.add_attendee("Alice")
private_event.add_attendee("Bob")

print(private_event.display_event())
print(public_event.display_event())

# Question 10. Write a code for Airline Reservation System using OOPS
class Flight:
    def __init__(self, flight_number, departure, arrival, dep_time, arr_time, available_seats, _id):
        self.flight_number = flight_number
        self.departure = departure
        self.arrival = arrival
        self.dep_time = dep_time
        self.arr_time = arr_time
        self.__available_seats = available_seats  
        self.__id = _id  

    def book_seat(self):
        if self.__available_seats > 0:
            self.__available_seats -= 1
            return "Seat booked successfully."
        else:
            return "No seats available."

    def cancel_reservation(self):
        self.__available_seats += 1
        return "Reservation cancelled."

    def remaining_seats(self):
        return self.__available_seats

    def display_flight(self):
        return f"Flight Number: {self.flight_number}, Departure: {self.departure}, Arrival: {self.arrival}, Available Seats: {self.__available_seats}"

class DomesticFlight(Flight):
    def __init__(self, flight_number, departure, arrival, dep_time, arr_time, available_seats, _id, airline):
        super().__init__(flight_number, departure, arrival, dep_time, arr_time, available_seats, _id)
        self.airline = airline

    def display_flight(self):
        return super().display_flight() + f", Airline: {self.airline}"

class InternationalFlight(Flight):
    def __init__(self, flight_number, departure, arrival, dep_time, arr_time, available_seats, _id, visa_required):
        super().__init__(flight_number, departure, arrival, dep_time, arr_time, available_seats, _id)
        self.visa_required = visa_required

    def display_flight(self):
        return super().display_flight() + f", Visa Required: {self.visa_required}"

domestic_flight = DomesticFlight("AI202", "Mumbai", "Delhi", "10:00 AM", "12:00 PM", 150, "DF123", "Air India")
international_flight = InternationalFlight("BA101", "Mumbai", "London", "02:00 PM", "07:00 PM", 200, "IF456", True)

print(domestic_flight.display_flight())
print(international_flight.display_flight())

print(domestic_flight.book_seat())
print(f"Remaining seats: {domestic_flight.remaining_seats()}")

print(international_flight.cancel_reservation())
print(f"Remaining seats: {international_flight.remaining_seats()}")


# Question 11. Define a Python module named constants.py containing constants like pl and the speed of light.

# Question 12. Write a Python module named calculator.py containing functions for addition, subtraction, multiplication, and division.

# Question 13. Implement a Python package structure for a project named ecommerce, containing modules for product management and order processing.

# Question 14. Implement a Python module named string_utils.py containing functions for string manipulation, such as reversing and capitalizing strings.

# Question 15. Write a Python module named file_operations.py with functions for reading, writing, and appending data to a file.

# Question 16. Write a Python program to create a text file named "employees.txt" and write the details of employees, including their name, age, and salary, into the file.
employees = [
    {"name": "John Doe", "age": 30, "salary": 50000},
    {"name": "Jane Smith", "age": 25, "salary": 60000},
    {"name": "Jim Brown", "age": 35, "salary": 55000},
]

with open('employees.txt', 'w') as file:
    for emp in employees:
        file.write(f"Name: {emp['name']}, Age: {emp['age']}, Salary: {emp['salary']}\n")


# Question 17. Develop a Python script that opens an existing text file named "inventory.txt" in read mode and displays the contents of the file line by line.
with open('inventory.txt', 'r') as file:
    for line in file:
        print(line.strip())


# Question 18. Create a Python script that reads a text file named "expenses.txt" and calculates the total amount spent on various expenses listed in the file.
total_expense = 0

with open('expenses.txt', 'r') as file:
    for line in file:
        total_expense += float(line.strip())

print(f"Total Expense: {total_expense}")

# Question 19. Create a Python program that reads a text file named "paragraph.txt" and counts the occurrences of each word in the paragraph, displaying the results in alphabetical order.
from collections import Counter

with open('paragraph.txt', 'r') as file:
    words = file.read().lower().split()

word_count = Counter(words)

for word, count in sorted(word_count.items()):
    print(f"{word}: {count}")


# Question 38.Anova Test:To study the performance of three detergents and three different water temperatures the following whiteness readings were obtained with specially designed equipment.
import numpy as np
import scipy.stats as stats

data = {
    'Detergent_A': [57, 55, 67],
    'Detergent_B': [49, 52, 68],
    'Detergent_C': [54, 46, 58]
}

f_statistic, p_value = stats.f_oneway(data['Detergent_A'], data['Detergent_B'], data['Detergent_C'])

print(f"F-Statistic: {f_statistic}, P-Value: {p_value}")



# Question 39.How would you create a basic Flask route that displays "Hello, World!" on the homepage?

# Question 40.Explain how to set up a Flask application to handle form submissions using POST requests.

# Question 41. Write a Flask route that accepts a parameter in the URL and displays it on the page.

# Question 42.How can you implement user authentication in a Flask application?

# Question 43.Describe the process of connecting a Flask app to a SQLite database using SQLAlchemy.

# Question 44.How would you create a RESTful API endpoint in Flask that returns JSON data?

# Question 45.Explain how to use Flask-WTF to create and validate forms in a Flask application.

# Question 46.How can you implement file uploads in a Flask application?

# Question 47.Describe the steps to create a Flask blueprint and why you might use one.

# Question 48.How would you deploy a Flask application to a production server using Gunicorn and Nginx?

# Question 49. Make a fully functional web application using flask, Mangodb. Signup, Signin page. And after successfully login Say hello Geeks message at webpage.