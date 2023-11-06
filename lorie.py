print("NO 1")

chenn_karaktè = "Jodia Se Gros Koze Nan La Repiblik"
miniskil = chenn_karaktè.lower()
print(miniskil)

print("NO 2")
chenn = "Haiti pap Peri Viv Haiti"
lis_espas = chenn.split()
print("afiche lis ki gen chak eleman yo",lis_espas)

print("NO 3")

chenn = "Isit la nou vann poul🐤🐥🐤🐥"
nouvo_chenn = " ".join([mo[0].upper()+ mo[1:] for mo in chenn.split])
print("mete tout premye lèt chak mo en majiskil:",nouvo_chenn)

print("NO 4")

chenn = "Maman a remis tous ses devoirs"
mo_komanse = "".join([mo[0] for mo in chenn.split()])
print("rekipere premye lèt chak mo epi afiche yo",mo_komanse)

print("NO 5")

chenn = "Haiti est un pays montagneux"
nouvo_chenn = chenn.replace("a","@")
print(nouvo_chenn)

print("NO 6")

chenn_1 = "ayiti"
chenn_2 = chenn_1[:: -1]


nouvo_chenn_majikil = chenn_2.upper()
print(nouvo_chenn_majikil)

print("NO 7")

chenn = " jodia nou jwenn tout sa ki bon"
endeks = chenn.find("a")
print("endeks premye kakraktè 'a':",endeks)


print("NO 8")

chenn = "ayiti dwea gn lajan"
total_endeks_a = chenn.lower().count('a')
print(total_endeks_a)

print("NO 9")

chenn ="sa se yon chenn ak A aparèy a lot a nan li"
endeks_a = [i for i,letter in enumerate(chenn)if letter == 'a']
print(endeks_a)

print("NO 10")

chenn ="nou prè pou tout bagay kap vini ."
chenn_san_espas =chenn.replace("","")
kantite_karaktè = str(len(chenn))
nouvo_chenn = chenn_san_espas + kantite_karaktè
print(nouvo_chenn)

print("partie 2 : Master List Union & Intersection & lis comprehension")

print("NO 1")

n = 40
lis_divizib = [i for i in range(n+1) if i % 2]
print("kreye yon lis eleman ki divizib pa 2,nan entèval[0-N]:",lis_divizib)

print("NO 2")

liste_entier = [1, 2, 3,4 ,5]
liste_chaine =[str(x) for x in liste_entier]
print("konvèti lis antye an yon lis chenn:",liste_chaine)

print("NO 3")

liste_chaine_miniscule =["janvier","fevrier","mars","avril","mai"]
liste_chaine_majuscule = [mo.upper() for mo in liste_chaine_miniscule]
print("konvèti lis chenn majiskil en miniskil:",liste_chaine_majuscule)

print("NO 4")

liste =[10,20,30,40,50,60,70,80,90]
nouvo_liste = [elem for i,elem in enumerate(lis) if i % 3 == 0]
print("kreye yon lis ki divizib pa 3 yo selman:",nouvo_liste)

print("NO 5")

liste_element =[1, 2, 3, 4, 5, 6, 7, 8, 9]
nouvo_liste =[tuple(liste_element[i:i+3]) for i in range(0,len(liste_element),3)]
print("liste ki gn chak 3 eleman yo nan yon TIPL:",nouvo_liste)





print("NO 6")
dictionnaire = {
    "clef 1" : "23"
    "clef 2" : " 12"
    "clef 3" : "78"
}
 dictionnaire_underscore = {k:f"_{v}_"if insintance(v,str)else v for k,v in dictionnaire.items()}
 print(dictionnaire_underscore)

print("NO 7")
dictionnaire ={
    "clef 1":"V2",
    "clef 2": "12313",
    "clef 3": "348",
    "clef ": "v4",
}
nouvo_dictionnaire = {k: v for k, in dictionnaire.items() if v.isdigit()}
print(nouvo_dictionnaire)


print("No 8")
dictionnaire ={
    "clef 1": "valeur 1",
    "clef 2": "valeur 2",
    "clef 3": "valeur 3",
}
liste_TIPL = [(k,v) for k,v in dictionnaire.items()]
print(liste_TIPL)

print("NO 9")
liste_TIPL =[('clef 1','034'),('clef 2','039'),('clef3','234')]
dictionnaire = dict(liste_TIPL)

print(dictionnaire)


print("NO 10")
dictionnaire 1 ={
    "clef 1":"109",
    "clef 2":"213",
    "clef 3":"980",
}
dictionnaire 2 = {
    "clef 2":"21",
    "clef 4":"23",
    "clef 5":"29",

}
nouvo_dictionnaire = {k: v for k, v in dictionnaire.items()}
nouvo_dictionnaire.update({k: v for k, v in dictionnaire2.items()})
print(nouvo_dictionnaire)


print("Partie 3 : Master Dictionnaire 😃😀😀 (isinstance ,Eval)")

print("NO 1")
dictionnaire ={
    "clef 1":"123",
    "clef 2":"879",
    "clef 3":"231",
}
liste_valeur =[v for k,v in dictionnaire.items()]

print(liste_valeur)

print("NO2")
valeur = input("entrer un mot avec acolade devant ak derrière: ")
while not (valeur.startswitch('{')and valeur.endswitch('}')):
    print(" la valeur n'a pas d'acolade .essayer une autre fois. ")
    valeur = input("entrer une valeur avec un acolade devant et derrière: ")

    print("valeur a correcte: ", valeur)
    
    print("NO 3")
    dictionnaire ={
        "clef 1": "12",
        "clef 2": "1'",
        "clef 3": "17",
    }

clef_a =liste(dictionnaire.keys())
print(clef_a)

print("NO 4")
dictionnaire ={
    "clef 1": "89",
    "clef 2": "87",
    "clef 3": "09",

}

valeur_a =liste(dictionnaire.values())
print(valeur_a)


print("No 5")

dictionnaire_original ={
    "clef 1": "23",
    "clef 1": "28",
    "clef 3": "39",
}
copie_dictionnaire =dictionnaire_original.copy()
 print(copie_dictionnaire)


 print("NO 6")
dictionnaire ={
    "clef 1": "12",
    "clef 2": "21",
    "clef 3": "90",
}
for k,v in dictionnaire.items():
    if isinstances(v,str):
        dictionnaire[k] = f"_{v}_"
        print(dictionnaire)

        print("NO 7")
        dictionnaire_original ={
            "clef1": "valeur1",
            "clef2": "123",
            "clef3": "456",
            "clef4": "valeur4",
        }

nouvo_dictionnaire ={k:v for k, v in dictionnaire_original.items() if v.isdigit()}
 print(nouvo_dictionnaire)



print("NO 8")
dictionnaire ={
    "clef1": "90",
    "clef2": "34",
    "clef3": "09",
}

liste_TIPL = [(k,v) for k, v in dictionnaire.items()]
print(liste_TIPL)

print("NO 9")

liste_TIPL = [('clef1','valeur1'),('clef2,'valeur2'),('clef3','valeur3')]
dictionnaire = dict(liste_TIPL)

print("NO 10")
dictionnaire1 ={
    "clef2": "valeur 22",
    "clef4": "valeur 32",
    "clef5": "valeur 34",
}

print("Partie 4")
print("MASTER FUNCTION CONCEPT")

print("NO 1")
def mot_inverse(mot):
mot_inverse = mot[::-1]
return mot_inverse

mot_input = input("tape yon mo: ")
mot_convertis = mot_inverse(mot_input)
print("l'inverse du mot est :" mot_convertis)

print("NO 7")

def cript_mo(mot):
alphabet ="abcdefghijklmnopqrstuvwxyz"
mot_cript = []

for caract in mot:
    caract = caract.lower()
    if caract in alphabet:
endeks =alphabet.index(caract)
mot_cript.append(str(endeks))

code_cript = '-'.join(mot_cript)
return code_cript

mot_input = input("entrer un mot:")
mot_cript = cripté_mo(mot_input)
print("code cript: ",mot_cript)


 print("NO 8")

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

print("NO 10")

def initial_non(non):
    non_separe = non.split()
    initial = ""
    
    for fraz in non_separe:
        initial_non += fraz[0].upper()  

    return initial

non_input = input("Tape yon non: ")
initial = initial_non(non_input)
print("Initial yo:", initial)














