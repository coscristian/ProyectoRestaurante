from matplotlib.font_manager import json_dump
import json

work_days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']

food_menu = {
    'Sopa':[
        ('Lunes', {'Sancocho Trifasico':15000}, {'Ajiaco':7000},{'Fideos':6300}),
        ('Martes', {'Sancocho Valluno':8500}, {'Cuchuco con espinazo':7200}, {'Guandú':9300}),
        ('Miercoles', {'Mazamorra':8000}, {'Mote de queso':5000}, {'Mondongo':9200}),
        ('Jueves', {'Sancocho de pescado':8400}, {'Sopa de patacón':5900}, {'Sopa de verduras':3700}),
        ('Viernes',{'Frijoles':7900}, {'Lentejas':9300}, {'Sopa de arroz':8000})
    ]
    ,
    'Principio':[
        ('Lunes',{'Yuca frita':4650},{'Buñuelos de platano maduro':3550},{'Plátanos calados':2750}),
        ('Martes',{'Papas con salsa':2300},{'Chicharron':5150},{'Dulce de leche':6650}),
        ('Miercoles',{'Salsa de ajo':1700},{'Pastel':6650},{'Ceviche de camarones':3850}),
        ('Jueves',{'Platano asado':3450},{'Empanada':1650},{'Papa rellena':7950}),
        ('Viernes',{'Buñuelo':800},{'Aborrajado':4650},{'Coctel de camarones':6250})
    ],
    'Carne':[
        ('Lunes',{'Sudado de carne de Res': 8450},{'Sudado de albondigas': 6450},{'Albondigas': 6940}),
        ('Martes',{'Bistec encebollado': 6450},{'Estofado de Res': 6450},{'Carne chimichurri': 8450}),
        ('Miercoles',{'Sudado de cola': 7450},{'Sobrebarriga': 8950},{'Chuzo de carne de res': 4450}),
        ('Jueves',{'Bistec a caballo': 4950},{'Bistec a la criolla': 7450},{'Carne desmechada': 7450}),
        ('Viernes',{'Carne con champiñones': 8950},{'Guiso de cola': 6950},{'Posta negra': 6950})
    ],
    'Ensalada':[
        ('Lunes',{'Ensalada de langosta':14660},{'Ensalada de chucho fresco':22660},{'Ensalada de repollo y piña':12660}),
        ('Martes',{'Ensalada bugueña':22660},{'Ensalada de cidra-papa':22660},{'Ensalada de calamar':13560}),
        ('Miercoles',{'Ensalada de corazones de lechuga':14660},{'Ensalada de pepino':12660},{'Ensalada de remolacha':14660}),
        ('Jueves',{'Ensalada de pollo':22660},{'Ensalda de caracol':12660},{'Ensalada de papaya verde':12660}),
        ('Viernes',{'Ensalada de pulpo':11660},{'Ensalada de espinacas':22660},{'Ensalada de atún':24660})
    ],
    'Jugo':[
        ('Lunes',{'Jugo de mango':7300},{'Jugo de mora':7300},{'Jugo de maracuya':5300}),
        ('Martes',{'Jugo de guayaba':6300},{'Jugo de piña':6300},{'Jugo de naranja':6300}),
        ('Miercoles',{'Limonada':6500},{'Jugo de lulo':4840},{'Salpicon':7840}),
        ('Jueves',{'Limonada de coco':4840},{'Jugo de guanabana':4840},{'Jugo de manzana':4740}),
        ('Viernes',{'Avena':5300},{'Café':1500},{'Pintadito':2000})
    ]
}

"""
Orders (dict) contains all the order asked by the user with its corresponding table number
orders = {'Table number 1': [('food', price, amount), ('food', price, amount), ...],
          'Table number 2': [('food',price, amount), ('food',price, amount), ...]
        ...
        } 
"""
orders = {}

def calculate_total_price(table_order: list):
    """
    Calculates the total price to pay in the specified table
    Parameters
    ----------
        table_order (list): List of tuples which contains all the orders of the identified table.
    Returns
    ---------
        int: Total price to pay
    """
    price_by_food = list(map(lambda tuple_food: tuple_food[1] * tuple_food[2], table_order))
    return sum(price_by_food)

def delete_table(table_number: int):
    """
    Deletes the specified table by its number
    Parameters
    ----------
        table_number (int): Identifier for the table to delete
    """
    del orders[table_number]

def total_of_orderes_by_table(table_number: int):
    """
    Checks how many orderes has a table
    Parameters
    ----------
        table_number (int): Identifier for the table
    Returns
    ----------
        int: The cuantity of orderes of the specified table
    """
    return len(orders[table_number])

def delete_order_by_index(table_order: list, table_number: int, order_to_delete: int):
    """"
    Deletes the selected order by the user
    Parameters
    ----------
        table_order (list): List of tuples which contains all the orders of the identified table.
        order_to_delete (int): Identifier o number of the order that the user wants to delete.
    """
    orders[table_number].pop(order_to_delete)

def is_valid_option_modify_order(selected_option: int):
    """
    Checks out if the user input is correct according to the specified options in the menu
    Parameters
    ----------
        selected_option (int): Option that the user has selected from the menu that modifies an registered order of a table
    Returns
    ---------
        bool: True if the option selected by the user is 1 or 2
    """
    return True if 1 <= selected_option <= 2 else False

def there_are_registered_tables():
    """
    Checks out if there is at least one registered table
    Returns:
    --------
        bool: True if there's at least one registered table
    """
    return True if len(orders) > 0 else False

def load_file(file_path: str = "ordenes.json"):
    """
    Loads the information from the file, then converts the json string identifier for the registered tables into int
    Parameters:
    -----------
        file_path (str): Name of the file to read
    Raises:
    -----------
        Exception: Exception raised if any error occurs
    """
    try:
        global orders
        with open(file_path) as json_file:
            orders = json.load(json_file)
    except:
        with open(file_path, "w") as json_file:
            json.dump({}, json_file)    
    orders = {int(k): v for k,v in orders.items()} #Converts the json string indentifier for the table into int

def write_file(file_path: str = "ordenes.json"):
    """
    Writes the registered tables and their ordersinformation on the file
    Parameters:
    -----------
        file_path (str): Name of the file to read
    Raises:
    -----------
        Exception: Exception raised if any error occurs
    """
    try:
        with open(file_path, 'w') as json_file:
            json.dump(orders, json_file, indent=2)
    except:
        raise Exception("No fue posible guardar la información en el archivo.")

def get_table_order(table_number: int):
    """"
    Get the list of orders that has been asked for
    Parameters
    -----------
        table_number (int): Identifier for the table
    Returns
    -----------
        list: List of tuples which contains all the orders of the identified table
    """
    for table, food in orders.items():
        if table == table_number:
            return food

def table_exists(table_number: int):
    """"
    Verifies if the number of the introduced exist
    Parameters
    -----------
        table_number (int): Identifier for the table
    Returns
    -----------
        bool: True if the number of table is registered, otherwise returns False
    """
    return True if table_number in orders else False

def save_order(table_number: int, value_to_order: int, amount: int, food_for_today: list):
    """
    Saves in the orders (dict:global) the food that the user has asked for, if the table exists, the food is saved in that specific key (table_number)
    Parameters:
    -----------
        table_number (int): Identifier for the table in the restaurant
        value_to_order (int): Identifier for the order(food) that the user asked for
        food_for_today (list): List of tuples which contains the food for the day
    Returns:
    -----------
        str: Saved Successfully
    """
    counter = 1
    for dict_of_food in food_for_today:
        for food, price in dict_of_food.items():
            if counter == value_to_order:
                try:
                    orders[table_number].append((food,price,amount)) #En caso de que la mesa ya haya realizado pedidos, agrega a la lista de tuplas, una tupla con el pedido nuevo
                except:
                    orders[table_number] = [(food,price,amount)]  #Si la mesa no ha realizado pedidos (No hay campo mesa para el diccionario)
            counter+=1

def get_food_for_today(food_per_week: list, today: str):
    """
    Get all the posible food depending on the day and the user selected option
    Parameters:
    -----------
        food_per_week (list): List of tuples which contain the day and the food for that day
        today (str): Day selected randomly
    Returns:
    -----------
        list: List of dicts which contains the food as key and the price as value
    """
    for tuple_of_food in food_per_week:
        if tuple_of_food[0] == today:
            return list(tuple_of_food[1:])

def convert_num_to_order(value: int) -> list:
    """
    Converts the num into an order
    Parameters:
    -----------
        value (int): Identifier for the order that the user has selected
    Returns:
    -----------
        list: List tuples which contains all the of food per week
    """
    counter = 1
    for order in food_menu:
        if counter == value:
            return food_menu[order]
        counter+=1
