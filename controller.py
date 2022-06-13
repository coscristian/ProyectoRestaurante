import view as vw
import model as mdl
import random

today = mdl.work_days[random.randint(0, len(mdl.work_days) - 1)]

def principal_menu():
    try:
        main_loop = True
        while main_loop:
            op = vw.option_principal_menu()
            if op == 1:
                create_order()

            vw.wait_for_input()
            vw.clear_screen()
                
    except Exception as e:
        print(e)

def create_order():
    vw.clear_screen()
    vw.show_title("Adding an order")
    table_number = vw.read_user_int("Ingrese el numero de la mesa: ")
    flag = True
    while flag: #While to ask for 1 or more orders
        vw.show_food_menu(today, mdl.food_menu)
        value_to_order = vw.read_user_int("Qué deseas ordenar?: ")
        if 1 <= value_to_order <= len(mdl.food_menu):
            #Takes the selected option from the user and get all the food per week
            food_per_week = mdl.convert_num_to_order(value_to_order)
            #Depending on the day, gets the food to show
            food_for_today = mdl.get_food_for_today(food_per_week, today)          
            vw.show_food_for_today(food_for_today)
            #print(food_for_today)
            value_to_order = vw.verify_option(vw.read_user_int("Qué deseas ordenar?: "), len(food_for_today))
            mdl.save_order(table_number, value_to_order, food_for_today)
            #print(mdl.orders)
        else:
            vw.show_invalid("Número de pedido no existe")
        flag = True if vw.continue_ordering() else False

"""def list_tables():
    vw.show_title("Lista de Mesas del restaurante")
    mdl.read_tables()"""

