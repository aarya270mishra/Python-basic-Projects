import time

menu = {
    "Burger": 120,
    "Pizza": 250,
    "Pasta": 180,
    "French Fries": 90,
    "Sandwich": 100,
    "Momos": 80,
    "Coffee": 70,
    "Tea": 30,
    "Cold Drink": 50,
    "Ice Cream": 60
}

gst_price = 0.05
def cal_gst(order_total):
    return order_total * gst_price 

order_total = 0
ordered =[]



def print_receipt(ordered, order_total, gst):
    print("="*15 ,"RECEIPT" ,"="*15)
    print("ITEM\tQTY\tPRICE\tTOTAL")
    print("=" * 40)

    for order in ordered:
        print(order["item"], "\t", order["qty"], "\t", order["price"], "\t", order["total"])

    print("--------------------------------------------------")
    print("Subtotal :", order_total)
    print("GST (5%) :", gst)
    print("Grand Total :", order_total + gst)
    print("--------------------------------------------------")



print("---------------WELCOME TO PYTHON RESTURANT---------------------")
time.sleep(2)



print("""---------------MENU-------------
    Burger : 120 \n
    Pizza : 250 \n
    Pasta : 180 \n
    French Fries : 90 \n
    Sandwich : 100 \n
    Momos : 80 \n
    Coffee : 70 \n
    Tea : 30 \n
    Cold Drink : 50 \n
    Ice Cream : 60\n """)

time.sleep(3)

while(True):
    item = input("Enter the Item You would like to order! ").title()
    qty = int(input("Enter Quantity"))
    if qty <=0:
        print("Quantity must be positive.")
        continue


    if item in menu:
        order_total += menu[item]* qty
        print(f"Your {item} has been added")

        ordered.append({
            "item": item,
            "qty": qty,
            "price": menu[item],
            "total":qty * menu[item]
        })

    else:
        print(f" Ordered item ,{item} is not available in the menu.")   

    another_item = input("Would you like to order more item (yes/no)?").lower()
    if another_item not in ["yes","no"]:
        break


        print("Please enter yes or no")
               
       
    if another_item=='no':
        print("Thank You for Considering Python resturant")

        gst = cal_gst(order_total)
        
    
        print_receipt(ordered,order_total,gst)
        break

