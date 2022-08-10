"""
Ground Shipping - a small flat charge plus a rate based on the weight of your package.
Ground Shipping Premium - a much higher flat charge, but you aren’t charged for weight.
Drone Shipping (new) - has no flat charge, but the rate based on weight is triple the rate of ground shipping.
"""

weight = 41.5
cost = 0.00

# Ground Shipping
if weight <= 2:
  cost += 20 + (weight*1.50)
elif weight <= 6:
  cost += 20 + (weight*3)
elif weight <= 10:
  cost += 20 + (weight*4)
elif weight > 10:
  cost += 20 + (weight*4.75)

print("Cost of Ground Shipping: $" + str(cost))

# Ground Shipping Premium
cost_prem = 125

print("Cost of Ground Shipping Premium: $" + str(cost_prem))

dcost = 0.00

# Drone Shipping
if weight <= 2:
  dcost += weight*4.50
elif weight <= 6:
  dcost += weight*9
elif weight <= 10:
  dcost += weight*12
elif weight > 10:
  dcost += weight*14.25

print("Cost of Drone Shipping: $" + str(dcost))
