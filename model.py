
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
        ('Lunes','Sudado de carne de Res','Sudado de albondigas','Albondigas'),
        ('Martes','Bistec encebollado','Estofado de Res','Carne chimichurri'),
        ('Miercoles','Sudado de cola','Sobrebarriga','Chuzo de carne de res'),
        ('Jueves','Bistec a caballo','Bistec a la criolla','Carne desmechada'),
        ('Viernes','Carne con champiñones','Guiso de cola','Posta negra')
    ],
    'Ensalada':[
        ('Lunes','Ensalada de langosta','Ensalada de chucho fresco','Ensalada de repollo y piña'),
        ('Martes','Ensalada bugueña','Ensalada de cidra-papa','Ensalada de calamar'),
        ('Miercoles','Ensalada de corazones de lechuga','Ensalada de pepino','Ensalada de remolacha'),
        ('Jueves','Ensalada de pollo','Ensalda de caracol','Ensalada de papaya verde'),
        ('Viernes','Ensalada de pulpo','Ensalada de espinacas','Ensalada de atún')
    ],
    'Jugo':[
        ('Lunes','Jugo de mango','Jugo de mora','Jugo de maracuya'),
        ('Martes','Jugo de guayaba','Jugo de piña','Jugo de naranja'),
        ('Miercoles','Limonada','Jugo de lulo','Salpicon'),
        ('Jueves','Limonada de coco','Jugo de guanabana','Jugo de manzana'),
        ('Viernes','Avena','Café','Pintadito')
    ]
}

"""
Orders (dict) contains all the order asked by the user with its corresponding table number
orders = {'Table number 1': [('food', price), ('food',price), ...],
          'Table number 2': [('food',price), ('food',price), ...]
        ...
        } 
"""
orders = {} 

def save_order(table_number: int, value_to_order: int, food_for_today: list):
    """
    Saves in the orders (dict:global) the food that the user has asked for
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
                    orders[table_number].append((food,price)) #En caso de que la mesa ya haya realizado pedidos, agrega a la lista de tuplas, una tupla con el pedido nuevo
                except:
                    orders[table_number] = [(food,price)]  #Si la mesa no hay realizado pedidos (No hay campo mesa para el diccionario)
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

def read_tables(table_id = None):
    """
    Reads all the tables registered
    Parameters:
    -----------
        table_id (int)[Optional]: Identifier for every table
    Returns:
    -----------
        list: List of tables with their orderes
    """
