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
spisok=loe_failist_listisse("Texfailedega.txt")
print(spisok)
def salvesta_failisse(file:str):
	f=open(file,"a")
	text=input("Sisesta tekst:")
	f.write(text+"\n")
	f.close()
for i in range(10):
	salvesta_failisse("loetelu.txt")

def faili_sisu_umberkirjutamine(file:str):
	text=input("sisesta uus tekst:")
	with open(file,"w") as f:
		f.write(text+"\n")
faili_sisu_umberkirjutamine(input("Faili nimetus")+".txt")
