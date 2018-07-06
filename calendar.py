import datetime
l={}
k=[]
f=[]
h=[]
b=[]
s=[]
ñ=[]
p=0
g=0
data=open("datos.txt","r+")
d=datetime.date.today().day
m=datetime.date.today().month
y=datetime.date.today().year
for line in data:
	x=str(line)
	for i in line:	
		g+=1
		k.append(i)
		if g==2:
			l.update({"sd"})
			break
	if k==[]:
		print()
	else:
		for i in line:
			if i==":":
				f.append(" ")
			else:
				f.append(i)
for i in f:
	if i!=" ":
		h.append(i)
	elif i==" ":
		break
s=f[::-1]
for i in s:
	if i==" ":
		break
	else:
		b.append(i)
ñ=b[::-1]
q=("".join(ñ))
w=("".join(h))
print("El día de hoy es: " + str(d)+ "/" +str(m)+ "/" + str(y))
n=int(input("Si desea ver los pendientes pulse 1 y si desea añadir una fecha pulse 2: "))
if n==1:
 if l=={}:
	 print("No hay eventos")
 else:
 	print("tienes "+ q+ " el "+ w)
elif n==2:
	i=str(input("Nombre: "))
	j=str(input("Fecha: "))
	l.update({j:i})
	data.write(j+":"+i)
	data.write("")
	print(l)
else:
	print("no hemos añadido esa función")
data.close()
