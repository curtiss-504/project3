import random 
import string 

chenn_karaktè = "Jodia Se Gros Koze Nan La Repiblik"
miniskil = chenn_karaktè.lower()
print(miniskil)


chenn = "Haiti pap Peri Viv Haiti"
lis_espas = chenn.split()
print("afiche lis ki gen chak eleman yo",lis_espas)

chenn = " Isit la nou vann poul🐥🐤🐥🐤."
nouvo_chenn = " ".join([mo[0].upper()+ mo[1:] for mo in chenn.split()])
print("mete tout premye lèt chak mo en majiskil:",nouvo_chenn)

chenn = "Maman a remis tous ses devoirs😊😉 "
mo_komanse = " ".join([mo[0] for mo in chenn.split()])
print("rekipere premye lèt chak mo epi afiche yo:",mo_komanse)


chenn = "Haiti est un pays montagneux🙄😶"
nouvo_chenn = chenn.replace("a","@")
print(nouvo_chenn)

chenn_1 = "ayiti"
chenn_2 = chenn_1[::-1]

nouvo_chenn_majiskil = chenn_2.upper()
print(nouvo_chenn_majiskil)



chenn = "jodia nou jwenn tout sa ki bon"
endeks = chenn.find("a")
print("Endeks premye karaktè 'a':", endeks)


chenn = "ayiti dwea gn lajan "
total_endeks_a = chenn.lower().count('a')
print(total_endeks_a)




chenn = "Ayiti kapab vanse"
endeks_a = [i for i, letter in enumerate(chenn) if letter == 'a']
print(endeks_a)



chenn = "nou prè pou nou f sa nou vle ."
chenn_san_espas = chenn.replace(" ", "")
kantite_karaktè = str(len(chenn))
nouvo_chenn = chenn_san_espas + kantite_karaktè
print(nouvo_chenn)

print("partie 2 : MASTER LIST Union & Intersection & Lis comprehension")

n = 40 
lis_divizib = [i for i in range(n+1) if i % 2 == 0]
print("kreye yon lis eleman ki divizib pa 2, nan entèval[o-N]",lis_divizib)


lis_antye = [1, 2, 3, 4, 5]
lis_chenn = [str(x) for x in lis_antye]
print("konvèti lis antye an yon lis chenn:",lis_chenn)



lis_chenn_miniskil = ["jan", "fevriye", "mas", "avrèl"]
lis_chenn_majiskil = [mo.upper() for mo in lis_chenn_miniskil]
print("konvèti lis chenn majiskil en miniskil:",lis_chenn_majiskil)


lis = [10, 20, 30, 40, 50, 60, 70, 80, 90]
nouvo_lis = [elem for i, elem in enumerate(lis) if i % 3 == 0]
print("kreye yon lis ki divizib pa 3 yo selman :",nouvo_lis)


lis_eleman = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
nouvo_lis = [tuple(lis_eleman[i:i+3]) for i in range(0, len(lis_eleman), 3)]
print("liste ki gn chak 3 eleman yo nan yn TIPL :",nouvo_lis)


diksyonè = {
    "kle1": "valeur1",
    "kle2": "valeur2",
    "kle3": "valeur3",
}

diksyonè_ak_underscore = {k: f"_{v}_" if isinstance(v, str) else v for k, v in diksyonè.items()}
print(diksyonè_ak_underscore)


diksyonè = {
    "kle1": "valeur1",
    "kle2": "123",
    "kle3": "456",
    "kle4": "valeur4",
}

nouvo_diksyonè = {k: v for k, v in diksyonè.items() if v.isdigit()}

print(nouvo_diksyonè)



diksyonè = {
    "kle1": "valeur1",
    "kle2": "valeur2",
    "kle3": "valeur3",
}

lis_avek_tipl = [(k, v) for k, v in diksyonè.items()]

print(lis_avek_tipl)




lis_avek_tipl = [('kle1', 'valeur1'), ('kle2', 'valeur2'), ('kle3', 'valeur3')]
diksyonè = dict(lis_avek_tipl)

print(diksyonè)



diksyonè1 = {
    "kle1": "valeur1",
    "kle2": "valeur2",
    "kle3": "valeur3",
}

diksyonè2 = {
    "kle2": "valeur22",
    "kle4": "valeur4",
    "kle5": "valeur5",
}

nouvo_diksyonè = {k: v for k, v in diksyonè1.items()}
nouvo_diksyonè.update({k: v for k, v in diksyonè2.items()})

print(nouvo_diksyonè)


print(" partie 3 : Master Dictionnaire  ☺☺☺☺ (Isinstance,Eval)")

print("Number 1")
diksyonè = {
    "kle1": "valeur1",
    "kle2": "valeur2",
    "kle3": "valeur3",
}

lis_valè = [v for k, v in diksyonè.items()]

print(lis_valè)



print("NO 3")
diksyonè = {
    "kle1": "valeur1",
    "kle2": "valeur2",
    "kle3": "valeur3",
}

kle_yo = list(diksyonè.keys())
print(kle_yo)

print("NO 4")
diksyonè = {
    "kle1": "valeur1",
    "kle2": "valeur2",
    "kle3": "valeur3",
}

valè_yo = list(diksyonè.values())
print(valè_yo)


print("NO 5")
diksyonè_orijinal = {
    "kle1": "valeur1",
    "kle2": "valeur2",
    "kle3": "valeur3",
}

kopi_diksyonè = diksyonè_orijinal.copy()

print(kopi_diksyonè)


print("NO 6")
diksyonè = {
    "kle1": "valeur1",
    "kle2": 123,
    "kle3": "valeur3",
}

for k, v in diksyonè.items():
    if isinstance(v, str):
        diksyonè[k] = f"_{v}_"

print(diksyonè)


print(" NO 7")
diksyonè_orijinal = {
    "kle1": "valeur1",
    "kle2": "123",
    "kle3": "456",
    "kle4": "valeur4",
}

nouvo_diksyonè = {k: v for k, v in diksyonè_orijinal.items() if v.isdigit()}

print(nouvo_diksyonè)


print ("no 8")
diksyonè = {
    "kle1": "valeur1",
    "kle2": "valeur2",
    "kle3": "valeur3",
}

lis_avek_tipl = [(k, v) for k, v in diksyonè.items()]

print(lis_avek_tipl)

print("NO 9")
lis_avek_tipl = [('kle1', 'valeur1'), ('kle2', 'valeur2'), ('kle3', 'valeur3')]
diksyonè = dict(lis_avek_tipl)

print(diksyonè)

print("NO 10 ")
diksyonè1 = {
    "kle1": "valeur1",
    "kle2": "valeur2",
    "kle3": "valeur3",
}

diksyonè2 = {
    "kle2": "valeur22",
    "kle4": "valeur4",
    "kle5": "valeur5",
}

nouvo_diksyonè = {k: v for k, v in diksyonè1.items()}
nouvo_diksyonè.update({k: v for k, v in diksyonè2.items() if k not in diksyonè1})

print(nouvo_diksyonè)


print ("Partie 4")
print("MASTER FUNCTION CONCEPT")


print("NO 1")
def mot_inverse(mot):
    mot_envès = mot[::-1]
    return mot_envès

mo_input = input("Tape yon mo kap gn pou ranvèse:  ")
mo_konvèti = mot_inverse(mo_input)
print("l'inverse du mot est :", mo_konvèti)


print("NO 7")

def kripte_mo(mot):
    alfabe = "abcdefghijklmnopqrstuvwxyz"
    mot_kripte = []
    
    for karakter in mot:
        karakter = karakter.lower()  # Konvèti karaktè yo nan miniskil
        if karakter in alfabe:
            endeks = alfabe.index(karakter)
            mot_kripte.append(str(endeks))
    
    kòd_kripte = '-'.join(mot_kripte)
    return kòd_kripte

mo_input = input("Tape yon mo: ")
mo_kripte = kripte_mo(mo_input)
print("Kòd kripte: ", mo_kripte)




def dekripte_mo(kòd_kripte):
    alfabe = "abcdefghijklmnopqrstuvwxyz"
    kòd_separe = kòd_kripte.split('-')
    mo_dekripte = ""
    
    for endeks_str in kòd_separe:
        if endeks_str.isnumeric():
            endeks = int(endeks_str)
            if 0 <= endeks < len(alfabe):
                lèt = alfabe[endeks]
                mo_dekripte += lèt
    
    return mo_dekripte

kòd_input = input("Tape kòd kripte: ")
mo_dekripte = dekripte_mo(kòd_input)
print("Mo dekripte: ", mo_dekripte)




def inisyal_non(non):
    non_separe = non.split()
    inisyal = " "
    
    for fraz in non_separe:
        inisyal += fraz[0].upper()  # Pran premye lèt nan chak fraz epi mete l' an majiskil

    return inisyal

non_input = input("Tape yon non: ")
inisyal = inisyal_non(non_input)
print("Inisyal yo:", inisyal)



