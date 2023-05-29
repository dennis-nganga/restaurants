#!/usr/bin/env python3

# tools/debug.py

from lib.customer import Customer
from lib.restaurant import Restaurant
from lib.review import Review

# Create some customers
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

# Create some restaurants
restaurant1 = Restaurant("Restaurant A")
restaurant2 = Restaurant("Restaurant B")

# Add reviews
customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 3)

# Test the methods
print(customer1.full_name())  # Output: John Doe
print(customer2.restaurants())  # Output: [Restaurant A]
print(restaurant1.average_star_rating())  # Output: 3.5
print(Customer.find_by_name("John Doe"))  # Output: <Customer object at 0x...>
print(Customer.find_all_by_given_name("John"))  # Output: [<Customer object at 0x...>]
