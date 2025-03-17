weight = 1.6
ground_flat = 20
drone_flat = 0
premium_flat = 125


''' Ground Shipping '''
def calculate_ground_shipping(weight):
    if weight <= 2:
        price_per_lb = 1.5
    elif weight <= 6:
        price_per_lb = 3
    elif weight <= 10:
        price_per_lb = 4
    else:
        price_per_lb = 4.75

    return price_per_lb * weight + ground_flat

''' Ground Shipping '''
def calculate_drone_shipping(weight):
    if weight <= 2:
        price_per_lb = 4.5
    elif weight <= 6:
        price_per_lb = 9
    elif weight <= 10:
        price_per_lb = 12
    else:
        price_per_lb = 14.25
    return price_per_lb * weight + drone_flat

def calculate_quote(weight):
  ground_shipping_cost = calculate_ground_shipping(weight)
  drone_shipping_cost = calculate_drone_shipping(weight)
  print(f"Ground shipping cost for {weight} lb: ${ground_shipping_cost}")
  print(f"Drone shipping cost for {weight} lb: ${drone_shipping_cost}")
calculate_quote(weight)

print(f"The premium shipping rate is ${premium_flat}")