#Producto con 2 datos (nombre, stock)
#Listado de productos desordenados. ¿Se pueden repetir los productos?
#Condicional, si el producto tiene menos de 10 elementos en stock, necesitara abastecimiento
#Obtener un listado con los productos con los productos con menor stock
#Actualizar el stock de los productos

products = [("manzana",15),("naranja",20),("platano",12),("fresa",28),("uva",18),("pera",2),("kiwi",10),("naranja",25),("manzana",30),("fresa",4),("kiwi",1)]
low_stock = []
for product in products:
    #Falta sumar los productos que se repiten
    if product[1] < 10:
        low_stock.append(product)
        low_stock.sort(key=lambda x: x[1])
        
for element in low_stock:
    print(f"-{element[0]}")
 