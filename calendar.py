def entrar():
  print("Hola, bienvenido a la experiencia Calendario de supervivencia universitario de UTEC")
  print("Elige una opcion")
  print("(1) Tengo una cuenta")
  print("(2) Registrarme")
  n= int(input("Cual?"))
  if n == 2:
    inscribirse(curso)
  elif n == 1:
    print("Que quieres hacer?")
    input()
curso=[]
def inscribirse(curso):
    print("Iniciando proceso de registro")
    nombre=str(input("cual es tu nombre?"))
    print("Hola", nombre)
    ciclo= input("En que ciclo estas")
    n= int(input("Cuantos cursos llevas?"))
    print("A continuacion ingresa tus cursos segun el orden de prioridad que deseas otorgarles")
    for i in range (n):
      print(i+1,"curso:")
      curso.append(input())
    print ("Gracias por tu preferencia")
    

curso=[]
entrar()
#pon entrar
#vacia tareas
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
      

      
import datetime

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

#hasta aqui
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
