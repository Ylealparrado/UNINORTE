import sys

print("BIENVENIDO A LA TIENDA UNINORTE")
print("por favor elegir cantidad de productos que desea llevar")
print("")
Producto1 = input("Cuantas libras de arroz desea 2000c/u")
ValorP1= int(Producto1) * 2000
Producto2 = input("Cuantas libras de papa desea 1000c/u")
ValorP2= int(Producto2) * 1000
Producto3 = input("Cuantas libras de yuca desea 4000c/u")
ValorP3= int(Producto3) * 4000
Producto4 = input("Cuantas libras de mora desea 3000c/u")
ValorP4= int(Producto4) * 3000
print("")
print("resumen pedido")
print("Va llevar arroz por valor de:", int(ValorP1))
print("Va llevar papa por valor de:", int(ValorP2))
print("Va llevar yuca por valor de:", int(ValorP3))
print("Va llevar mora por valor de:", int(ValorP4))
print("Total valor compra:", int(ValorP1+ValorP2+ValorP3+ValorP4))
