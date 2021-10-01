# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?
the_little_mermaid = 3
brother_bear = 5
hercules = 1
movie_rental_ttl = (the_little_mermaid + brother_bear + hercules) * 3
print(movie_rental_ttl

# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
google  = 400 * 6
amazon = 380 * 4
facebook = 350 * 10
my_pay = google + amazon + facebook
print(my_pay)

# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.
class_not_full = True
schedule_conflict = False
can_student_be_enrolled = class_not_full and not schedule_conflict
print(can_student_be_enrolled)

# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.
purchase_amt = 3
expired = False
premium_member = True
offer_applied = purchase_amt >= 3 and not expired or premium_member
print(offer_applied)

# Create a variable that holds a boolean value for each of the following conditions:
# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace

pw_five_characters = True
user_20_plus_chars = True
pw_different = True
user_and_pw_valid = pw_five_characters and user_20_plus_chars and pw_different
print(user_and_pw_valid)






