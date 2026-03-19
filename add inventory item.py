# add inventory item 


# The counter start at 1000
id_counter = 1000

def add_inventory_item():
    """
    Prompts staff for item details and generates a unique Item ID.
    Returns a dictionary containing all item information.
    """
    global id_counter # Use the global counter to ensure to call the id_counter in the code
    

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


item_name,item_id,quantity, price_per_item = add_inventory_item()

print("Adding Inventory Item\n") 
print("Item Name :", item_name)
print("Iteam ID:" ,item_id)
print ("Quantity :" ,quantity)
print("price_per_Item :",price_per_item )
