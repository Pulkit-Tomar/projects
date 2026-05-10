original_price = 100
discount_percentage = 20
sales_tax_rate = 0.08

discount_amount = original_price * (discount_percentage / 100)
discounted_price = original_price - discount_amount
sales_tax = discounted_price * sales_tax_rate
final_price = discounted_price + sales_tax

print(final_price)
