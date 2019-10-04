import csv
from operator import itemgetter
from creator import file_creator

data = csv.DictReader(open('orders.csv'))

sellers = {}
brands = {}

'''
El siguiente bucle trata de obtener el id del vendedor (seller) y el nombre de marca,
si existe, suma la comision total (ya existente) + comision e la linea que esta iterando
si no existe, crea el objeto para poder re utilizarlo
'''
for row in data:
    seller = sellers.get(row['seller_id'])
    brand = brands.get(row['brand_name'])

    seller_comission = float(row['price']) * float(row['seller_commission_percent'])  # Calcula la comision por cada fila
    elena_comission = float(row['price']) * 0.12
    brand_comission = float(row['price']) - seller_comission - elena_comission - float(row['logistic_cost'])

    if seller:
        seller['total_comission'] += seller_comission
    else:
        sellers[row['seller_id']] = {
            'seller_id': row['seller_id'],
            'total_comission': seller_comission
        }

    if brand:
        brand['total_revenue'] += brand_comission
    else:
        brands[row['brand_name']] = {
            'brand_name': row['brand_name'],
            'total_revenue': brand_comission
        }

# Variables para crear el archivo que calcula comisiones para las embajadoras
fields = ['seller_id', 'total_comission']
order_options = lambda x: int(itemgetter(0)(x))

# Calcular comisiones embajadoras
file_creator(sellers, 'ambassadors.csv', fields, order_options)

# Variables para crear el archivo que calcula comisiones para las marcas
fields = ['brand_name', 'total_revenue']
order_options = lambda x: str(itemgetter(0)(x))

# calcular comisiones de marca
file_creator(brands, 'brands.csv', fields, order_options)
print('Se ha completado el proceso!')