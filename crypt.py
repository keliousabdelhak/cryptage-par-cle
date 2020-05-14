alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def crypter(txt):
	txt_chiffre=""
	for i in txt:
		txt_chiffre+=alphabet[alphabet.index(i)+10]
	return txt_chiffre



tableau_txt=[]
def text_a_crypter(txt):
	for i in txt:
		try:
			tableau_txt.append([i,alphabet.index(i)])
		except:
			tableau_txt.append([i," "])
	return tableau_txt




tableau_cle=[]
def cle(txt):
	for i in txt:
		tableau_cle.append([i,alphabet.index(i)])
	t=len(tableau_txt)-len(tableau_cle)
	k=0
	ind=0
	while k<t:
		tableau_cle.append([" ",alphabet.index(tableau_cle[ind][0])])
		if ind < 3:
			ind+=1
		else:

			ind=0
		k+=1
	return tableau_cle


tableau_crypt=[]
tab=[]
def crypter_cle(txt,clem):
	text=text_a_crypter(txt)
	clee=cle(clem)
	sup=0
	for i in text:
		tab.append([i,clee[sup]])
		sup+=1

	for i in tab:
		try:
			if i[0][1]+i[1][1]<=26:
				tableau_crypt.append([i[0][1]+i[1][1],alphabet[i[0][1]+i[1][1]]])
			elif i[0][1]+i[1][1]>26:
				tableau_crypt.append([i[0][1]+i[1][1]-26,alphabet[i[0][1]+i[1][1]-26]])
		except:
			tableau_crypt.append([" "," "])


la_clee="ANIS"
le_texte="ELITECH CONTEST"
crypter_cle(le_texte,la_clee)
print("texte a crypter :")
print(tableau_txt)
print("\n")
print("la cle de cryptage :")
print(tableau_cle)
print("\n")
print("texte chiffré :")
print(tableau_crypt)
print("\n")

txt_crypt=""
for i in tableau_crypt:
	txt_crypt+=i[1]

print("texte avant cryptage :",le_texte)
print("texte après cryptage :",txt_crypt)