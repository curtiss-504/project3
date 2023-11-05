chenn_karaktè = "Jodia Se Gros Koze Nan La Repiblik"
miniskil = chenn_karaktè.lower()
print(miniskil)


chenn = "Haiti pap Peri Viv Haiti"
lis_espas = chenn.split()
print(lis_espas)

chenn = "Isit la nou vann poul🐤🐥🐤🐥"
nouvo_chenn = " ".join([mo[0].upper()+ mo[1:] for mo in chenn.split])
print(nouvo_chenn)

chenn = "Maman a remis tous ses devoirs"
mo_komanse = "".join([mo[0] for mo in chenn.split()])
print(mo_komanse)

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

