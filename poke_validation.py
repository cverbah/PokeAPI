# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 19:47:27 2022

@author: c_ver
"""
import re 

with open("pokemon_list.txt", "r") as f:
    pokemon_lista = f.readlines()

pokemon_lista = [elemento.strip('\n') for elemento in pokemon_lista]

def validate_pokemon():
    ''''returns a valid pokemon name in the list '''
    selection = input('Por favor ingrese el pokemon que desea checkear  : ')
    selection = selection.lower()
    selection = ''.join(re.findall('[a-zA-Z\-.]',selection)) #removing everything excep letters,- and . 
    selection = selection.replace('.','-')   
    if selection =='codigo-cero':
        selection = 'type-null'
    
    while True:
        if selection in pokemon_lista:
            break
        else:
            print('')
            print('El pokemon no se encuentra en la lista. En caso de existir espacios, por favor cambielo por un - .(Ejemplo: mr mime escriba mr-mime ')
            selection = input('Por favor ingrese el pokemon que desea checkear: ')
            selection = selection.lower()
            selection = ''.join(re.findall('[a-zA-Z\-.]',selection )) #removing everything excep letters,- and . 
            selection = selection.replace('.','-')          
            if selection =='codigo-cero':
                selection = 'type-null' 
                
    print('Cargando...')
    return selection

