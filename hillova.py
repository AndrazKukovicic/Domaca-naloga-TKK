import timeit
#Prebere besedilo iz datoteke in odstrani presledke in nove vrstice, vrne pa string.
def preberi_kriptogram(file_path):
    with open(file_path, 'r', encoding='utf-8') as dat:
        text = dat.read()
        text = text.replace('\n', '').replace(' ', '')
        return text

#Funkcija, ki pretvori crke v številke, kjer je a=0, b=1, ..., z=25. Vrne list števil.
def crke_v_stevilke (text):
    return [ord(crka) - ord('a') for crka in text]

#Funkcija, ki pretvori številke v crke, kjer je 0=a, 1=b, ..., 25=z. Vrne list crk.
def stevilke_v_crke (stevilke):
    list = []
    x = ord('a')
    for stevilo in stevilke:
        list.append(chr(int(stevilo) + x))
    return list
 
#def naredi_bloke(text, dolzina):
    return [list(text[i:i+dolzina]) for i in range(0, len(text), dolzina)]

#def bloki_v_text(bloki):
    flat_list = [item for sublist in bloki for item in sublist]
    return ''.join(stevilke_v_crke(flat_list))

def desifriraj (kriptogram):  
    for h1 in range(0,26):
        for h2 in range(0,26):
            for h3 in range(0,26):
                for h4 in range(0,26):
                    if (h1*h4 - h2*h3) % 26 != 0:   #Determinanta različna od 0, matrika mora biti obrnljiva.
                        resitev = []
                        for i in range(0, len(kriptogram), 2):
                            a = kriptogram[i]
                            b = kriptogram[i+1]
                            resitev.append((a*h1 + b*h3) % 26)
                            resitev.append((a*h2 + b*h4) % 26)
                        
                        resitev = stevilke_v_crke(resitev)
                        resitev = ''.join(resitev)
                        if 'the' in resitev  and 'and' in resitev and 'crypto' in resitev: #Ugibam, da se bodo te besede pojavile v besedilu.
                            print(resitev)
                            print(h1, h2, h3, h4)
                            

#Zagon programa.
file_path = 'kriptogram.txt'
kriptogram_stevilke = crke_v_stevilke(preberi_kriptogram(file_path))
desifrirano_besedilo = desifriraj(kriptogram_stevilke)

timeit(desifrirano_besedilo)