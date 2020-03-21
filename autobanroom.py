def main():
	Dataset = input("Podaj Powod Bana : ")
	spl_word = 'Powód:'
	spl_word2 = 'Gracz:'
	spl_word3 = 'Zablokowany przez:'
	spl_word4 = 'Czas trwania:'
	res = Dataset.partition(spl_word)[2] 
	sep = '('
	sep2 = ')'
	sep3 = ','
	rest = res.split(sep, 1)[0]
	powod = rest
	res2 = Dataset.partition(spl_word2)[2]
	gracz = res2.split(sep2, 1)[0]
	res3 = Dataset.partition(spl_word3)[2]
	banujacy = res3.split(sep3, 1)[0]
	res4 = Dataset.partition(spl_word4)[2]
	czas = res4.split(sep2, 1)[0]
	f_discordable1 = "```Kto:{banneduser} \nPrzez:{banner} \nPowod:{reason} \nCzas:{time} \nMO : -```".format(banneduser=gracz, banner=banujacy, reason=powod, time=czas)
	print(f_discordable1)
#main loop
while 1 == 1:
	main()
