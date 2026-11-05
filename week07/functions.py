def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")


def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price


print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
total = discounted + tax

print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${total:.2f}")


def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax_amount = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax_amount


result = final_price(200, "gold", 0.07)
print(f'final_price(200, "gold", 0.07) = ${result:.2f}')   

orders = [
    (200, "gold"),
    (150, "silver"),
    (80, "bronze"),
    (500, "none")
]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

x = 100  # Global variable


def double_it():
    x = 999  # Local variable
    return x * 2

print(x)
print(double_it())
print(x)
   