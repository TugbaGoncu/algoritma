import re
def parcalara_ayir(metin):
    # Özel isimlere dikkat ederek metni parçalara ayırma
    parcalar = re.findall(r'\b[A-Z][a-z]+\b|\b\w+\b', metin)
    birlesik_parcalar = []
    indeks = 0

    while indeks < len(parcalar):
        #seslenme ögesi
        if indeks < len(parcalar) - 1 and parcalar[indeks + 1][0].isupper():
            birlesik_parcalar.append(parcalar[indeks] + ' ' + parcalar[indeks + 1])
            indeks += 2
        else:
            #Bağlaç
            if parcalar[indeks] == "de":
                birlesik_parcalar.append(parcalar[indeks-1] + ' ' + parcalar[indeks])
                birlesik_parcalar.remove(parcalar[indeks-1])
                indeks += 1
            #İşaret zamiri
            elif parcalar[indeks]=="bu":
                birlesik_parcalar.append(parcalar[indeks] + ' ' + parcalar[indeks + 1])
                indeks += 2
            birlesik_parcalar.append(parcalar[indeks])
            indeks += 1

    return birlesik_parcalar


metin = "Merhaba Ali, bu akşam seni geçerken görüp ekonomiyi de konuşmak istiyorum."
parcalar = parcalara_ayir(metin)
print(parcalar)
