# Exercise 1.2. Write Python code to evaluate these expressions.
# The answers can be stored in a name, or evaluated in a print statement

# 1. How many seconds are there in 42 minutes 42 seconds?

seconds = (42 * 60) + 42

# 2. How many miles are there in 10 kilometers? Hint: there are 1.61
# kilometers in a mile.

miles = 10 / 1.61

# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your
# average pace (time per mile in minutes and seconds)? What is your average
# speed in miles per hour?

# time / mile
avg_pace_sec = seconds  / miles
avg_pace_min = (seconds / 60) / miles
avg_speed_mph = avg_pace_min / 60