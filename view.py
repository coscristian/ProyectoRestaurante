import os

def show_menu_modify_order():
    print()
    show_title("Menu para modificar pedido")
    print("1. Agregar pedido a la mesa seleccionada")
    print("2. Eliminar pedido de la mesa seleccionada")
    print("-"*25)

def show_specific_table_number(table_number: int):
    print(f"Ordenes de la mesa {table_number}")

def show_header_order():
    print("="*90)
    header = f"{'ID':>3s} {'Pedido':40s} {'Estado':15s} {'Precio Unitario(COP)':<20s} {'Cantidad':<2s}"
    print(header)
    print("-"*len(header))

def show_table_order(table_order: list, table_number: int):
    show_title(f"Pedidos de la mesa {table_number}")
    show_header_order()
    counter = 1
    for food_tuple in table_order:
        print(f"{counter:>3d} {food_tuple[0]:40s} {'Pendiente':15s} ${food_tuple[1]:,}{'':<15s} {food_tuple[2]:<2d}")
        counter+=1
    print()

def verify_option(user_input: int, limit_value: int) -> int:
    invalid_value = True
    flag_first_time_error = False
    while invalid_value:
        if flag_first_time_error:
            user_input = read_user_int("Qué deseas ordenar?: ")
        if 0 < user_input <= limit_value:
            invalid_value = False
        else:
            show_invalid("Número de pedido no existe")
            flag_first_time_error = True
    return user_input

def show_food_for_today(food_for_today: list):
    counter = 1
    for food_dict in food_for_today:
        for food, price in food_dict.items():
            print(f"\t{counter}. {food} --> {price}")
            counter+=1

def show_invalid(message: str):
    print()
    print(f"{message}")
    print("x"*len(message))
    print()

def show_food_menu(day: str, food_menu: dict):
    show_title("Opciones de pedido")
    print(f"Día de hoy: {day}")
    counter = 0
    for order_option in food_menu:
        counter+=1
        print(f"{counter}. {order_option}")

def wait_for_input():
    input("Presione una tecla para continuar...")

def clear_screen():
    os.system('clear')

def ask_user_for_bool_input(message: str) -> bool:
    answer = input(message)     
    if answer == "s" or answer == "S":
        return True
    elif answer == "n" or answer == "N":
        return False
    else:
        print("Ingrese una opcion valida")
        return True

def input_order() -> dict:
    
    order = {'estado':'pendiente'}

def show_title(title=''):
    print()
    print(title.upper())
    print("-"*len(title))

def read_user_int(message = "Seleccione una opción: ") -> int:
    valid_input = False
    while not valid_input:
        try:
            v = int(input(message))
            valid_input = True
        except:
            print("")
            print("-"*30)
            print("Ingrese un valor numerico valido.")
            print("-"*30)
            print("")
    return v

def option_principal_menu() -> int:
    show_title("Restaurante el corrientazo")
    show_title("Menu principal")
    print("1. Adicionar pedido")
    print("2. Consultar una mesa")
    print("3. Listar mesas")
    print("4. Modificar pedido de mesa")
    print("5. Eliminar mesa")
    print("6. Calcular valor total a pagar")
    print("7. Actualizar estado de mesa a pagado")
    print("8. Salir del sistema")
    print("-"*25)
    return read_user_int()