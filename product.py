# Catalog with product names and prices
catalog = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

# Discount rules
discount_rules = {
    "flat_10_discount": {"threshold": 200, "discount_amount": 10},
    "bulk_5_discount": {"threshold": 10, "discount_percentage": 5},
    "bulk_10_discount": {"threshold": 20, "discount_percentage": 10},
    "tiered_50_discount": {"quantity_threshold": 30, "single_product_threshold": 15, "discount_percentage": 50}
}

# Fees
gift_wrap_fee = 1
shipping_fee_per_package = 5
items_per_package = 10

# Initialize variables
subtotal = 0
total_discount = 0
total_gift_wrap_fee = 0
total_shipping_fee = 0

# Get quantity and gift wrap information for each product
for product, price in catalog.items():
    quantity = int(input(f"Enter the quantity of {product}: "))
    gift_wrap = input(f"Is {product} wrapped as a gift? (yes/no): ")

    # Calculate product amount
    product_amount = price * quantity

    # Apply bulk discount if applicable
    if quantity > discount_rules["bulk_5_discount"]["threshold"]:
        product_amount -= (product_amount * discount_rules["bulk_5_discount"]["discount_percentage"]) / 100

    # Calculate gift wrap fee
    if gift_wrap.lower() == "yes":
        gift_wrap_fee_total = gift_wrap_fee * quantity
        total_gift_wrap_fee += gift_wrap_fee_total
        product_amount += gift_wrap_fee_total

    # Update subtotal
    subtotal += product_amount

    # Apply flat discount if applicable
    if subtotal > discount_rules["flat_10_discount"]["threshold"]:
        total_discount += discount_rules["flat_10_discount"]["discount_amount"]

# Calculate shipping fee
total_shipping_fee = (subtotal // items_per_package) * shipping_fee_per_package

# Apply bulk discount if total quantity exceeds threshold
if sum(quantity for quantity in catalog.values()) > discount_rules["bulk_10_discount"]["threshold"]:
    total_discount += (subtotal * discount_rules["bulk_10_discount"]["discount_percentage"]) / 100

# Apply tiered discount if applicable
if (
    sum(quantity for quantity in catalog.values()) > discount_rules["tiered_50_discount"]["quantity_threshold"]
    and any(quantity > discount_rules["tiered_50_discount"]["single_product_threshold"] for quantity in catalog.values())
):
    quantity_above_threshold = sum(quantity - discount_rules["tiered_50_discount"]["single_product_threshold"]
                                   for quantity in catalog.values() if quantity > discount_rules["tiered_50_discount"]["single_product_threshold"])
    discount_amount = (catalog["Product A"] * discount_rules["tiered_50_discount"]["discount_percentage"]) / 100
    total_discount += discount_amount * quantity_above_threshold

# Calculate total
total = subtotal - total_discount + total_gift_wrap_fee + total_shipping_fee

# Output details
for product, price in catalog.items():
    quantity = int(input(f"Enter the quantity of {product}: "))
    gift_wrap = input(f"Is {product} wrapped as a gift? (yes/no): ")

    # Calculate product amount
    product_amount = price * quantity

    # Apply bulk discount if applicable
    if quantity > discount_rules["bulk_5_discount"]["threshold"]:
        product_amount -= (product_amount * discount_rules["bulk_5_discount"]["discount_percentage"]) / 100

    # Calculate gift wrap fee
    if gift_wrap.lower() == "yes":
        gift_wrap_fee_total = gift_wrap_fee * quantity
        total_gift_wrap_fee += gift_wrap_fee_total
        product_amount += gift_wrap_fee_total

    # Update subtotal
    subtotal += product_amount

    # Apply flat discount if applicable
    if subtotal > discount_rules["flat_10_discount"]["threshold"]:
        total_discount += discount_rules["flat_10_discount"]["discount_amount"]

# Calculate shipping fee
total_shipping_fee = (subtotal // items_per_package) * shipping_fee_per_package

# Apply bulk discount if total quantity exceeds threshold
if sum(quantity for quantity in catalog.values()) > discount_rules["bulk_10_discount"]["threshold"]:
    total_discount += (subtotal * discount_rules["bulk_10_discount"]["discount_percentage"]) / 100

# Apply tiered discount if applicable
if (
    sum(quantity for quantity in catalog.values()) > discount_rules["tiered_50_discount"]["quantity_threshold"]
    and any(quantity > discount_rules["tiered_50_discount"]["single_product_threshold"] for quantity in catalog.values())
):
    quantity_above_threshold = sum(quantity - discount_rules["tiered_50_discount"]["single_product_threshold"]
                                   for quantity in catalog.values() if quantity > discount_rules["tiered_50_discount"]["single_product_threshold"])
    discount_amount = (catalog["Product A"] * discount_rules["tiered_50_discount"]["discount_percentage"]) / 100
    total_discount += discount_amount * quantity_above_threshold

# Calculate total
total = subtotal - total_discount + total_gift_wrap_fee + total_shipping_fee

# Output details
print("Product Details:")
for product, price in catalog.items():
    quantity = int(input(f"Enter the quantity of {product}: "))
    gift_wrap = input(f"Is {product} wrapped as a gift? (yes/no): ")
    product_amount = price * quantity
    if quantity > discount_rules["bulk_5_discount"]["threshold"]:
        product_amount -= (product_amount * discount_rules["bulk_5_discount"]["discount_percentage"]) / 100
    if gift_wrap.lower() == "yes":
        gift_wrap_fee_total = gift_wrap_fee * quantity
        total_gift_wrap_fee += gift_wrap_fee_total
        product_amount += gift_wrap_fee_total
    subtotal += product_amount
    if subtotal > discount_rules["flat_10_discount"]["threshold"]:
        total_discount += discount_rules["flat_10_discount"]["discount_amount"]
    print(f"{product}: Quantity: {quantity}, Total Amount: {product_amount}")

print("Summary:")
print(f"Subtotal: {subtotal}")
print(f"Discount Applied: flat_10_discount, Amount: {total_discount}")
print(f"Shipping Fee: {total_shipping_fee}")
print(f"Gift Wrap Fee: {total_gift_wrap_fee}")
print(f"Total: {total}")