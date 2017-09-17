# I attempted to do this instruction set in Codecademy, and would like to come back to understand it more thoroughly
# 1. Below your existing code, define a function called rental_car_cost with an argument called days.
# Calculate the cost of renting the car:
# Every day you rent the car costs $40.
# if you rent the car for 7 or more days, you get $50 off your total.
# Alternatively (elif), if you rent the car for 3 or more days, you get $20 off your total.
# You cannot get both of the above 

# This attempt failed:

def rental_car_cost(days):
  return days * 40          # I want to test if this will also interpret as the right answer in a console
  if days >= 7:
    return (days * 40) - 50
  elif days >= 3:
        return (days * 40) - 20
  return rental_car_cost

# This was the correct answer:

def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost
  
  # finished:
  
  # 1. Below your existing code, define a function called trip_cost that takes two arguments, city and days.
# Like the example above, have your function return the sum of calling the rental_car_cost(days), hotel_cost(days), 
# and plane_ride_cost(city) functions. It is completely valid to call the hotel_cost(nights) function with the variable days. 
# Just like the example above where we call double(n) with the variable a, we pass the value of days to the new function in 
# the argument nights.

def trip_cost(city, days):
  return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city)
  
  print trip_cost("Los Angeles", 5, 600)
  
  # => prints '1955' to console
