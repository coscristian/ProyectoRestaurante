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
                update_order() 
            elif op == 5:
                delete_table()
            elif op == 6:
                total_to_pay()
            elif op == 7:
                update_table_status()
            elif op == 8:
                main_loop = False
                vw.show_title("Saliendo del sistema...")
            vw.show_title()
            vw.wait_for_input()
            vw.clear_screen()
    except Exception as e:
        print(e)
    mdl.write_file()

def delete_table():
    vw.clear_screen()
    vw.show_title("Eliminar mesa")
    table_number_to_del = vw.read_user_int("Ingrese el numero de la mesa a eliminar: ")
    if mdl.table_exists(table_number_to_del):
        mdl.delete_table(table_number_to_del)
        vw.clear_screen()
        vw.show_title("Mesa eliminada correctamente")
    else:
        vw.clear_screen()
        vw.show_invalid("Numero de mesa no existe")

def create_order():
    vw.clear_screen()
    vw.show_title("Pidiendo orden")
    table_number = vw.read_user_int("Ingrese el numero de la mesa: ")
    ask_for_user_order(table_number)

def ask_for_user_order(table_number: int):
    flag = True
    while flag: #While to ask for 1 or more orders
        vw.clear_screen()
        vw.show_food_menu(today, mdl.food_menu)
        value_to_order = vw.read_user_int("Qué deseas ordenar?: ")
        if 1 <= value_to_order <= len(mdl.food_menu):
            #Takes the selected option from the user and get all the food per week
            food_per_week = mdl.convert_num_to_order(value_to_order)
            #Depending on the day, gets the food to show
            food_for_today = mdl.get_food_for_today(food_per_week, today)          
            vw.show_food_for_today(food_for_today)
            value_to_order = vw.verify_option(vw.read_user_int("Qué deseas ordenar?: "), len(food_for_today))
            amount = vw.read_user_int("Ingrese la cantidad de productos: ")
            mdl.save_order(table_number, value_to_order, amount, food_for_today)
            vw.clear_screen()
            vw.show_title('Orden guardada exitosamente')
        else:
            vw.clear_screen()
            vw.show_invalid("Número de pedido no existe")
        flag = True if vw.ask_user_for_bool_input("Deseas continuar ordenando? (s/n): ") else False

def consult_table():
    vw.clear_screen()
    vw.show_title("Consultando mesa")
    table_number = vw.read_user_int("Ingrese el numero de la mesa: ")
    #Debo verificar si la mesa existe para consultarla y mostrar todas las ordenes de ella
    if mdl.table_exists(table_number):
        vw.clear_screen()
        table_order = mdl.get_table_order(table_number)
        vw.show_table_order(table_order, table_number)
    else:
        vw.clear_screen()
        vw.show_invalid("Número de mesa no existe")

def list_tables():
    vw.clear_screen()
    if mdl.there_are_registered_tables():
        for registered_table, registered_food in mdl.orders.items():
            vw.show_table_order(registered_food, registered_table)
    else:
        vw.show_invalid("No hay mesas registradas en el momento.")

def delete_order(table_order: list, table_number: int):
    vw.clear_screen()
    vw.show_table_order(table_order, table_number)
    vw.show_title(f"Eliminar pedido de la Mesa {table_number}")
    order_to_delete = vw.read_user_int("Ingrese el ID del pedido que desea eliminar: ")
    if 1 <= order_to_delete <= len(table_order):
        mdl.delete_order_by_index(table_order, table_number, order_to_delete - 1)
        #If there are no more orders from that table
        if mdl.total_of_orderes_by_table(table_number) == 0:
            mdl.delete_table(table_number)
    else:
        vw.clear_screen()
        vw.show_invalid("ID ingresada no existe")

def update_order():
    vw.clear_screen()
    vw.show_title("Modificar pedido")
    table_number = vw.read_user_int("Ingrese el numero de la mesa en la que desea modificar el pedido: ")
    
    if mdl.table_exists(table_number):
        table_order = mdl.get_table_order(table_number)
        incorrect_option = True
        while incorrect_option:
            vw.clear_screen()
            vw.show_table_order(table_order, table_number)
            vw.show_menu_modify_order()
            selected_option = vw.read_user_int()
            if mdl.is_valid_option_modify_order(selected_option):
                incorrect_option = False
                if selected_option == 1:
                    ask_for_user_order(table_number)
                else:
                    delete_order(table_order, table_number)
            else:
                vw.clear_screen()
                vw.show_invalid("Opcion seleccionada es incorrecta.")
    else:
        vw.clear_screen()
        vw.show_invalid("Número de mesa no existe")

#Voy aquí, solo falta probar la actualización del estado
def update_table_status():
    vw.clear_screen()
    vw.show_title("Actualizar estado de mesa a pagado")
    table_number = vw.read_user_int("Ingrese el numero de la mesa: ")
    if validate_table(table_number):
        vw.clear_screen()
        vw.show_title(f"Al actualizar el estado a pagado se eliminará el registro de la mesa {table_number} en el sistema")
        user_answ = vw.ask_user_for_bool_input(f"¿Está seguro que desea actualizar el estado de la mesa {table_number} a pagado? (s/n): ")
        if user_answ:
            mdl.delete_table(table_number)
            vw.clear_screen()
            vw.show_title(f"El estado de la mesa {table_number} se actualizó a PAGADO y se eliminó la mesa del sistema")
        else:
            vw.clear_screen()
            vw.show_invalid(f"El estado de la mesa {table_number} no se actualizó a PAGADO")

def validate_table(table_number: int):
    if mdl.there_are_registered_tables():
        if mdl.table_exists(table_number):
            return True
        else:
            vw.clear_screen()
            vw.show_invalid("Numero de mesa invalido")
    else:
        vw.clear_screen()
        vw.show_invalid("No hay mesas registradas en el sistema")
    return False

def total_to_pay():
    vw.clear_screen()
    vw.show_title("Total a pagar")
    table_number = vw.read_user_int("Ingrese el numero de la mesa: ")
    if validate_table(table_number):
        table_order = mdl.get_table_order(table_number)
        total_value = mdl.calculate_total_price(table_order)
        vw.clear_screen()
        vw.show_table_order(table_order, table_number)
        vw.show_title(f"Precio total a pagar en la mesa {table_number} --> ${total_value:,}")
