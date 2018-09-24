# Number of cars
cars = 100

# Space/number of seats in each car
space_in_a_car = 4.0

# Number of drivers
drivers = 30

# Number of passengers
passengers = 90

# Number of cars not driven
cars_not_driven = cars - drivers

# Number of cars driven
cars_driven = drivers

# Maximum carpool capacity
carpool_capacity = cars_driven * space_in_a_car

# Average number of passengers per car
average_passengers_per_car = passengers / cars_driven

print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")

# Study Drills

# The reason for error: "NameError: name 'car_pool_capacity' is not defined" is because the variable is defined on line 7 as carpool_capacity, rather than car_pool_capacity. The extra underscore changes the variable name and means that it won't be recognised.

# Using 4.0 instead of 4 is not necessary but is more accurate.

