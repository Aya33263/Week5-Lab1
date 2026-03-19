#calculate total value task 1 +task 2


# The counter start at 1000
id_counter = 1000

def add_inventory_item():

    global id_counter # Use the global counter to ensure to call the id_counter in the code
    print("Adding Inventory Item:\n")

    # Handling staff inputs

    item_name =str(input("Item Name: "))
    
    # The requirement asks to return the generated ID automatically
    item_id = id_counter
    print(f"Item ID: {item_id}")
    
    quantity = int(input("Quantity: "))
    price_per_item = float(input("Price per Item: $"))
    
    # Increment the counter for the next item to ensure uniqueness
    id_counter += 1
    
    # Return all inputs as a dictionary (or a tuple if preferred)
    return item_name,item_id,quantity, price_per_item 

# here we add the task 2
 
def calculate_total_value():
    # Call the function from Task 1 "unpack" the returned values
    item_name, item_id, quantity, price_per_item = add_inventory_item()

    # Calculate the total value use this equation (Quantity * Price)
    total_value = quantity * price_per_item
 #"" :.2f "" we add this formats the number to 2 decimal places (e.g., $250.00)
    print(f"\nTotal Value: ${total_value:.2f}")
    return total_value
    

print (calculate_total_value())        
