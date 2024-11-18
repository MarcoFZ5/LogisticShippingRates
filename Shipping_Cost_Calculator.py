#Shipping cost calc

#Weight and Rate

weight = float(input("Enter package weight in KGs"))
rate = float(input("Enter shipping rate per KG"))

shipping_cost = weight*rate

print(f"Shipping cost: {shipping_cost} US")
