nombre=input("Ingrese el nombre del cliente : ")
dni=int(input("Ingrese el numero de dni : "))
cantidad=int(input("Ingrese la cantidad de productos : "))

total=0
fin="Cliente : "+nombre+"\nDNI : "+str(dni)+"\nProductos vendidos : "

print("******Solicitud de productos ******")
for i in range(1,cantidad+1):
    nomPro=input("Nombre del producto"+str(i)+ ":")
    cantidadV=int(input("Ingrese la cantidad vendida : "))
    precioU=float(input("Ingrese el precio unitario : "))

    monto=cantidadV*precioU
    total=total+monto
    fin=fin+"\n"+nomPro+":$"+str(cantidadV)+"*"+str(precioU)+"="+str(monto)

fin=fin+"\nTotal vendido : $. "+str(total)
print(fin)








