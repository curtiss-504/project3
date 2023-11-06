chenn_karaktè = "Jodia Se Gros Koze Nan La Repiblik"
miniskil = chenn_karaktè.lower()
print(miniskil)


chenn = "Haiti pap Peri Viv Haiti"
lis_espas = chenn.split()
print("afiche lis ki gen chak eleman yo",lis_espas)

chenn = "Isit la nou vann poul🐤🐥🐤🐥"
nouvo_chenn = " ".join([mo[0].upper()+ mo[1:] for mo in chenn.split])
print("mete tout premye lèt chak mo en majiskil:",nouvo_chenn)

chenn = "Maman a remis tous ses devoirs"
mo_komanse = "".join([mo[0] for mo in chenn.split()])
print("rekipere premye lèt chak mo epi afiche yo",mo_komanse)

chenn = "Haiti est un pays montagneux"
nouvo_chenn = chenn.replace("a","@")
print(nouvo_chenn)

chenn_1 = "ayiti"
chenn_2 = chenn_1[:: -1]


nouvo_chenn_majikil = chenn_2.upper()
print(nouvo_chenn_majikil)


chenn = " jodia nou jwenn tout sa ki bon"
endeks = chenn.find("a")
print("endeks premye kakraktè 'a':",endeks)



chenn = "ayiti dwea gn lajan"
total_endeks_a = chenn.lower().count('a')
print(total_endeks_a)


chenn ="sa se yon chenn ak A aparèy a lot a nan li"
endeks_a = [i for i,letter in enumerate(chenn)if letter == 'a']
print(endeks_a)


chenn ="nou prè pou tout bagay kap vini ."
chenn_san_espas =chenn.replace("","")
kantite_karaktè = str(len(chenn))
nouvo_chenn = chenn_san_espas + kantite_karaktè
print(nouvo_chenn)

print("partie 2 : Master List Union & Intersection & lis comprehension")

n = 40
lis_divizib = [i for i in range(n+1) if i % 2]
print("kreye yon lis eleman ki divizib pa 2,nan entèval[0-N]:",lis_divizib)

liste_entier = [1, 2, 3,4 ,5]
liste_chaine =[str(x) for x in liste_entier]
print("konvèti lis antye an yon lis chenn:",liste_chaine)


liste_chaine_miniscule =["janvier","fevrier","mars","avril","mai"]
liste_chaine_majuscule = [mo.upper() for mo in liste_chaine_miniscule]
print("konvèti lis chenn majiskil en miniskil:",liste_chaine_majuscule)

liste =[10,20,30,40,50,60,70,80,90]
nouvo_liste = [elem for i,elem in enumerate(lis) if i % 3 == 0]
print("kreye yon lis ki divizib pa 3 yo selman:",nouvo_liste)

liste_element =[1, 2, 3, 4, 5, 6, 7, 8, 9]
nouvo_liste =[tuple(liste_element[i:i+3]) for i in range(0,len(liste_element),3)]
print("liste ki gn chak 3 eleman yo nan yon TIPL:",nouvo_liste)





