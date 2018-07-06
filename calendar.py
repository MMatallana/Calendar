import datetime
d=datetime.date.today().day
m=datetime.date.today().month
y=datetime.date.today().year
print("El día de hoy es: " + str(d)+ "/" +str(m)+ "/" + str(y))
n=int(input("Si desea ver los pendientes pulse 1 y si desea añadir una fecha pulse 2: "))
l={}
k=[]
f=[]
h=[]
b=[]
s=[]
ñ=[]
u=[]
p=0
g=0
data=open("datos.txt","r+")
if n==1:
	for line in data:
		x=str(line)
		for i in line:	
			g+=1
			k.append(i)
			if g==2:
				break
		if k!=[]:
			for i in line:
				if i!=":":
					f.append(i)
				elif i==":":
					f.append(" ")
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
	for i in f:
		if i==" ":
			break
		else:
			u.append(i)
	ñ=b[::-1]
	j=len(data.readlines())
	q=("".join(ñ))
	w=("".join(u))
	if g==0:
		print("No hay eventos")
	else:
 		print("tienes "+ q + " el "+ w)
elif n==2:
	i=str(input("Nombre: "))
	v=str(input("Fecha: "))
	l.update({v:i})
	data.write(v+":"+i)
	data.write("\n")
	print(l)
else:
	print("no hemos añadido esa función")
data.close()
