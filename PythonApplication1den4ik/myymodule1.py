
import random
#Cоздаем функции
def loe_failist(file:str)->str:
	"""loeme tekst failist
	"""
	f=open(file,"r")
	stroka=f.read() #str 4itaet fail kak text primenjaja ne 4itaemie simvoli
	#stroka=f.readlines() #list sozdaet spisok s kazdoj novoj stro4ki
	f.close()
	return stroka
stroka=loe_failist("Texfailedega.txt")
print(stroka)
def loe_failist_listisse(file:str)->list:
	"""Loeme tekst failist ja salvesta järjendisse
	"""
	f=open(file,"r")
	list_=[]
	for stroka in f:
		list_.append(stroka.strip())
	f.close()
	return list_
def faili_sisu_umberkirjutamine(file:str,list_:list):
	with open(file,"w") as f:
		for slovo in list_:
			f.write(slovo+"\n")

def passautomat()->str:
	"""Пароль создается машиной
	"""	
	str0=".,:;!_*-+()/#¤%&"
	str1 = '0123456789'
	str2 = 'qwertyuiopasdfghjklzxcvbnm'
	str3 = str2.upper() # 'QWERTYUIOPASDFGHJKLZXCVBNM'
	str4 = str0+str1+str2+str3
	ls = list(str4) # список [".",",",":"...]
	random.shuffle(ls) #перемешаем
# Извлекаем из списка 12 произвольных значений
	psword = ''.join([random.choice(ls) for x in range(12)])
# Пароль готов
	return psword
def paskontroll(psword: str)->bool:
	ls=list(psword)
	for e in ls:
		if e.isdigit(): d=True
		if e.isalpha(): a=True
		if e.isupper(): u=True
		if e.islower():l=True
		if e in list(".,:;!_*-+()/#¤%&"): s=True
	if d==True and a==True and u==True and l==True and s==True:
		t=True
	else:
		t=False
	return t

def koik_kasutajad(users,passwords):
	i=0
	for users in users:
		print(users,end="-")
		print(passwords[i])
		i+=1

