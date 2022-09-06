import urllib.request

Slownik = { '1': [], '2': []}
while True:
    Liczba = input('1-Wielkosci podstawowe \n2-generacja zrodel wiatrowych i fotowoltaicznych\nWpisz "koniec", aby przejsc do nastepnej czesci programu \n-->')
    if Liczba == 'koniec':
        # print(Slownik)
        break
    elif Liczba == '1':
        Pierwsza_data=input('Podaj pierwsza data\n-->')
        Druga_data=input('Podaj druga data\n-->')
        Slownik['1'].append([Pierwsza_data, Druga_data])        
    else:
        Pierwsza_data=input('Podaj pierwsza data\n-->')
        Druga_data=input('Podaj druga data\n-->')
        Slownik['2'].append([Pierwsza_data, Druga_data])      

for daty1 in Slownik['1']:
    try:
        url1='https://www.pse.pl/getcsv/-/export/csv/PL_WYK_KSE/data_od/{z}/data_do/{k}'.format(z = daty1[0], k = daty1[1])
        nazwa_pliku = '{poczatek}-{koniec}'.format(poczatek = daty1[0], koniec = daty1[1])
        urllib.request.urlretrieve(url1, '1{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))
    except:
        print('Nieprawidłowa_data')

for daty2 in Slownik['2']:
    try:
        url2='https://www.pse.pl/getcsv/-/export/csv/PL_GEN_WIATR/data_od/{z}/data_do/{k}'.format(z = daty2[0], k = daty2[1])
        print(url2)
        nazwa_pliku = '{poczatek}-{koniec}'.format(poczatek = daty2[0], koniec = daty2[1])
        urllib.request.urlretrieve(url2, '2{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))
    except:
        print('Nieprawidłowa_data')