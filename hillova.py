# Read and print the text in kriptogram.txt
import numpy as np
print(np.__version__)

def preberi_kriptogram(file_path):
    with open(file_path, 'r', encoding='utf-8') as dat:
        text = dat.read()
        text = text.replace('\n', '').replace(' ', '')
        print(text)
        return text
def crke_v_stevilke (text):
    return [ord(crka) - ord('a') for crka in text]

def stevilke_v_crke (stevilke):
    return [chr(stevilo + ord('a')) for stevilo in stevilke]

def naredi_bloke(text, dolzina):
    return [list(text[i:i+dolzina]) for i in range(0, len(text), dolzina)]

def bloki_v_text(bloki):
    flat_list = [item for sublist in bloki for item in sublist]
    return ''.join(stevilke_v_crke(flat_list))
   


file_path = 'kriptogram.txt'


bloki_stevilk = naredi_bloke(crke_v_stevilke(preberi_kriptogram(file_path)), 2)
print(bloki_v_text(bloki_stevilk))

