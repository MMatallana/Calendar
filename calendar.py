lista=[['201720026','Acevedo Esquivel, Daniel Gonzalo',[14,6,14]],
['201720058','Castro Alejo, Carlos Piero',[0,0,7]],
['201720060','Crispin Flores, Carlos Jhack',[20,20,7]],
['201720061','Delgado Díaz, José Iván',[20,7,13]],
['201720031','Díaz Gardini, Andrea Gabriela',[14,13,20]],
['201720063','Ferruzo García, Sheryl Damarys',[6,10,7]],
['201720068','López Reyna, Miriam',[6,10,7]],
['201720072','Mendoza Baldarrago, Brayan Brus',[12,14,7]],
['201720075','Meza Cruzado, Tania Lisbet',[12,8,14]],
['201720076','Mory Reyes, Mayte Mirella',[6,15,7]],
['201720038','Mungi Osores, Andree Cristhian',[20,14,14]],
['201720039','Olabarrera Vilcatoma, José Manuel',[0,0,7]],
['201720041','Paz Coronel, Walter Alejandro',[14,9,7]],
['201720083','Polo Mendoza, Gabriela',[6,7,14]],
['201620053','Ponce Contreras, Luis Eduardo',[20,20,20]],
['201710641','Silva Calderón, Gonzalo Alejandro',[14,15,20]],
['201720090','Sime Costilla, William',[2,0,7]],
['201720107','Sánchez Paredes, Josué Andoni',[20,20,14]],
['201720046','Sánchez Albarracín, Guillermo Fernando',[20,20,14]],
['201720092','Tasayco Castilla, Marlyn Brenda',[12,4,0]],
['201720048','Velazco Champac, Geraldyne Eliane',[6,5,0]]]

def bubbleSort(lista):
  for num in range(len(lista) - 1, 0,-2):
    for j in range(num):
      prom2=(lista[j+1][2][0]+lista[j+1][2][1]+lista[j+1][2][2])/3
      prom1=(lista[j][2][0]+lista[j][2][1]+lista[j][2][2])/3
      if prom1>prom2:
        aux = lista[j]
        lista[j] = lista[j + 1]
        lista[j + 1] = aux
  print("MENORES NOTAS")
  print(lista[0][1])
  print(lista[1][1])
  print(lista[2][1])
  print("MAYORES NOTAS:")
  print(lista[20][1])
  print(lista[19][1])
  print(lista[18][1])

bubbleSort(lista)

import datetime
d=datetime.date.today().day
m=datetime.date.today().month
y=datetime.date.today().year
print("El día de hoy es: " + str(d)+ "/" +str(m)+ "/" + str(y))
l={}
f=[]
k=[]
h=[]
b=[]
s=[]
ñ=[]
u=[]
nombres=[]
d=0
p=0
g=0
data=open("datos.txt","r+")
reg=open("datos.txt","r+")
def entrar():
  print("Hola, bienvenido a la experiencia Calendario de supervivencia universitario de UTEC")
  print("Elige una opcion")
  print("(1) Tengo una cuenta")
  print("(2) Registrarme")
  n= int(input("Cual?"))
  if n == 2:
  	inscribirse(curso)
curso=[]
def inscribirse(curso):
    print("Iniciando proceso de registro")
    nombre=str(input("cual es tu nombre?"))
    print("Hola", nombre)
    nombres.append(nombre)
    n= int(input("Cuantos cursos llevas?"))
    print("A continuacion ingresa tus cursos segun el orden de prioridad que deseas otorgarles")
    for i in range (n):
      print(i+1,"curso:")
      curso.append(input())
    print ("Gracias por tu preferencia")

entrar()

Fisica1={ "Hito1":[8,7,"13042018"], 
"Hito2":[8,7,"04052018"],
"Hito3":[8,7,"18052018"]}
Matematica1={
"Quiz0.1":[1,7,"11042018"],
"Quiz1.1":[2,7,"11042018"],
"Quiz2.1":[4,3,"11042018"],
"Quiz0.1":[1,7,"11042018"],
"Quiz1.2":[2,7,"02052018"],
"Quiz2.2":[4,3,"02052018"], 
"Quiz0.2":[1,7,"02052018"],
"Quiz1.3":[2,7,"16052018"],
"Quiz2.3":[4,3,"16052018"], 
"Quiz0.3":[1,7,"16052018"]}

tareas={}
cursost=[Fisica1,Matematica1]
for a in range (len(curso)):
  if curso[a]=="Fisica1":
    tareas.update(Fisica1)
  elif curso [a]=="Matematica1":
    tareas.update(Matematica1)

findeciclo = datetime.date(2018, 7,7)
iniciodeciclo = datetime.date(2018, 3, 26)
diferencia = findeciclo - iniciodeciclo

fechas=[]
for g in range (103):
  gap=iniciodeciclo+datetime.timedelta(days=g)
  d= gap.day
  m= gap.month
  y= gap.year
  if int(d)<10 and int(m)<10:
    dia = str(d)
    mes = str(m)
    ano= str(y)
    fechas.append("0"+dia+"0"+mes+ano)
  elif int(d)<10 and int(m)>10:
    dia = str(d)
    mes = str(m)
    ano= str(y)
    fechas.append("0"+dia+mes+ano)
  elif int(d)>=10 and int(m)<10:
    dia = str(d)
    mes = str(m)
    ano= str(y)
    fechas.append(dia+"0"+mes+ano)
  else:
    dia = str(d)
    mes = str(m)
    ano= str(y)
    fechas.append(dia+mes+ano)

diasdelciclo={}
for t in range (len(fechas)):
  diasdelciclo.update({fechas[t]:[]})

def combinardiccionarios(tareas, diasdelciclo):
  for c in diasdelciclo.keys():
    valordellave=c
    t=[]
    for v in tareas.keys():
      r= tareas.get(v)
      if r[2]==valordellave:
        t.append(v)
        diasdelciclo.update({valordellave:t})
combinardiccionarios(tareas, diasdelciclo)
n=int(input("Si desea ver los pendientes pulse 1 y si desea añadir una fecha pulse 2: "))
reg.write(str(nombres))
reg.write("\n")
if n==1:
	for line in data:
		p+=1
		for i in line:
			g+=1
			k.append(i)
		u=k[::-1]
		for i in u:
			if i!=":":
				f.append(i)
			elif i==":":
				break
		for i in line:
			if i!=":":
				h.append(i)
			elif i==":":
				break
		s=f[::-1]
		q=("".join(s))
		w=("".join(h))
		if g==0:
			print("No hay eventos")
		else:
 			print("tienes "+ w + " el "+ q)
elif n==2:
	i=str(input("Nombre: "))
	v=str(input("Fecha: "))
	l.update({v:i})
	data.write(i+":"+v)
	data.write("\n")
else:
	print("no hemos añadido esa función")
data.close()
