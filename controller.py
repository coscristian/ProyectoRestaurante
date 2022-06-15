import view as vw
import model as mdl
import random

today = mdl.work_days[random.randint(0, len(mdl.work_days) - 1)]

def principal_menu():
    #Al cargar el archivo, debo guardar como entero el identificador de la mesa del archivo JSON, automaticamente JSON lo convierte a String
    mdl.load_file()
    try:
        main_loop = True
        while main_loop:
            op = vw.option_principal_menu()
            if op == 1:
                create_order()
            elif op == 2:
                consult_table()
            elif op == 3:
                list_tables()
            elif op == 4:
                update_order() #Voy aquí
                """
                Modificar orden va a permitir agregar o eliminar un pedido de una mesa
                registrada
                """
            elif op == 9:
                main_loop = False
            vw.show_title()
            vw.wait_for_input()
            vw.clear_screen()
    except Exception as e:
        print(e)
    mdl.write_file()

def create_order():
    vw.clear_screen()
    vw.show_title("Pidiendo orden")
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
            value_to_order = vw.verify_option(vw.read_user_int("Qué deseas ordenar?: "), len(food_for_today))
            mdl.save_order(table_number, value_to_order, food_for_today)
            vw.show_title('Orden guardada exitosamente')
        else:
            vw.show_invalid("Número de pedido no existe")
        flag = True if vw.continue_ordering() else False

def consult_table():
    vw.clear_screen()
    vw.show_title("Consultando mesa")
    table_number = vw.read_user_int("Ingrese el numero de la mesa: ")
    #Debo verificar si la mesa existe para consultarla y mostrar todas las ordenes de ella
    if mdl.table_exists(table_number):
        vw.clear_screen()
        vw.show_specific_table_number(table_number)
        vw.show_title_order()
        table_order = mdl.get_table_order(table_number)
        vw.show_table_order(table_order)
    else:
        vw.show_invalid("Número de mesa no existe")

def list_tables():
    vw.clear_screen()
    if mdl.there_are_registered_tables():
        for registered_table, registered_food in mdl.orders.items():
            vw.show_specific_table_number(registered_table)
            vw.show_title_order()
            vw.show_table_order(registered_food)
    else:
        vw.show_invalid("No hay mesas registradas en el momento.")

def update_order():
    pass

"""def list_tables():
    vw.show_title("Lista de Mesas del restaurante")
    mdl.read_tables()"""

