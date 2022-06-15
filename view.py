import os

def show_specific_table_number(table_number: int):
    print(f"Ordenes de la mesa {table_number}")

def show_title_order():
    print("="*35)
    print(f"{'Pedido':^10} {'Estado':^10} {'Precio (COP)':^10}")
    print("-"*35)

def show_table_order(table_order: list):
    for food_tuple in table_order:
        print(f"{food_tuple[0]:^10} {'Pendiente':^10} {food_tuple[1]:^10}")
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

def continue_ordering() -> bool:
    answer = input("Deseas continuar ordenando? (s/n): ")     
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
    print("-"*30)

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
    print("4. Actualizar pedido")
    print("5. Eliminar mesa")
    print("6. Eliminar pedido")
    print("7. Calcular valor total a pagar")
    print("8. Actualizar estado de una mesa")
    print("-"*25)
    return read_user_int()