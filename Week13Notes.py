products = {123:"Hammer", 846:"Wrench", 982:"Paintbrush"}

prod_id = 333

if prod_id in products:
    print(products[prod_id])
else:
    print("Products", prod_id, "not in dict")

new_prod_id = input("Enter new prod id: ")
new_prod_name = input("Enter new prod name: ")

products[new_prod_id] = new_prod_name

try:
    del products[777]
except KeyError:
    print("Product ID", prod_id, "is not in the dict")



print(products)