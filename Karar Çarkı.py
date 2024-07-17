import random

bölme=int(input("Kaç bölme istersiniz: "))
liste=[]
sayaç=0

for x in range(1,bölme+1):
    sayaç+=1
    x=input(f"{sayaç}.")
    liste.append(x)
    
sayı=random.randint(1,bölme)
print(liste[sayı-1])
