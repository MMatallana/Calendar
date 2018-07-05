import datetime
l={}
data=open("datos.txt","r+")
d=dd=datetime.date.today().day
m=datetime.date.today().month
y=datetime.date.today().year
for line in data:
	p=line.rstrip(":")
	o=line.lstrip(":")
	print(p)
	print(line)
	print(line.rstrip(":"))
l.update({p:o})
print("El día de hoy es: " + str(d)+ "/" +str(m)+ "/" + str(y))
n=int(input("Si desea ver los pendientes pulse 1 y si desea añadir una fecha pulse 2: "))
if n==1:
 print(l)
elif n==2:
	i=str(input("Nombre: "))
	j=str(input("Fecha: "))
	l.update({j:i})
	data.write(j+":"+i)
	print(l)
else:
	print("no hemos añadido esa función")
data.close()
