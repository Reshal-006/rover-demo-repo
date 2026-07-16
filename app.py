from auth import authenticate
from payment import calculate_discount

print(authenticate({}, "admin"))
print(calculate_discount(100, 0))