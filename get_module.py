# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 18:18:03 2022

@author: c_ver
"""

import requests
import json
import random
from PIL import Image
from urllib.request import urlopen
#Funciones
##Stats
def get_stats(pokemon_info):
    '''returns: dictionary containing the stats of the pokemon'''
    dict_stats = {}
    for stat in pokemon_info['stats']:

        stat_url = stat['stat']['url']
        es = translate_to_es(stat_url)
        dict_stats.update({es:stat['base_stat']})    
    return dict_stats

##Type
def get_types(pokemon_info):
    '''returns: list containing all the types. checks that is at most 2 types'''
    types_sp = []
    for t in pokemon_info['types']:
        url = t['type']['url']
        types_sp.append(translate_to_es(url))
    assert len(types_sp)==1 or len(types_sp)==2,"the pokemon must have 1 or 2 types"
    return types_sp

##Special Indicators
def get_special_indicators_prev_evo(pokemon_info):
    '''returns: list of the special indicators and previous evolution '''
    indicators_dict ={'is_baby':False, 'is_legendary': False, 'is_mythical': False}
    indicators_translate = []
    pokemon_id = pokemon_info['id']
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}"
    info = json.loads(requests.get(url).text)
    
    indicators_dict['is_baby'] = info['is_baby']
    indicators_dict['is_legendary'] = info['is_legendary']
    indicators_dict['is_mythical'] = info['is_mythical']
    if indicators_dict['is_baby'] == True:
        indicators_translate.append('Bebé')
        
    if indicators_dict['is_legendary'] == True:
        indicators_translate.append('Legendario')
    
    if indicators_dict['is_mythical'] == True:
        indicators_translate.append('Mítico')
    
    ##previous evolution
    try:
        previous_evolution = info['evolves_from_species']['name']
    except TypeError:
       previous_evolution = 'None' 

    return indicators_translate, previous_evolution

##Random Description
def get_random_description(pokemon_info):
    '''returns: random description of the pokemon'''
    pokemon_id = pokemon_info['id']
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}"
    info = json.loads(requests.get(url).text)
    descriptions = []
    for  t in info['flavor_text_entries']:
        if t['language']['name'] == 'es':
            descriptions.append(t['flavor_text'].replace('\n',' '))
            
    return random.choice(descriptions)

##Damages
def get_damages(pokemon_info):
    '''returns: the damage relations of the pokemon'''
    types_en = [] #types in english
    for t in pokemon_info['types']:
        types_en.append(t['type']['name'])

    for t in types_en:
        index = types_en.index(t)
        url = f"https://pokeapi.co/api/v2/type/{t}"
        info = json.loads(requests.get(url).text)
        if index == 0:
            keys = list(info['damage_relations'].keys())
            dict_damage_keys = {key: set() for key in keys} #creating the initial dictionary
        for i in info['damage_relations']:
            for j in info['damage_relations'][i]:
                #print(i,j['name'],translate_to_es(j['url']))
                dict_damage_keys[i].add(translate_to_es(j['url']))
    
    return(dict_damage_keys)

##Image url
def get_image_url(pokemon_info):
    if pokemon_info['sprites']['other']['official-artwork']:
        url = pokemon_info['sprites']['other']['official-artwork']
    return url['front_default']

##Translate to spanish
def translate_to_es(url):
    '''returns: translate the data into spanish'''
    req = requests.get(url)
    info = json.loads(req.text)
    for language in info['names']:
        if language['language']['name'] == 'es':        
            return language['name']

##Main: Get pokemon info
def get_pokemon_info(pokemon):
    pokemon_dict = {}
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    r = requests.get(url)
    #pokemon data
    pokemon_info = json.loads(r.text)
    pokemon_dict['name'] = pokemon_info['name']
    pokemon_dict['id'] = pokemon_info['id']
    pokemon_dict['weight'] = pokemon_info['weight']
    pokemon_dict['height'] = pokemon_info['height']
    pokemon_dict['stats'] = get_stats(pokemon_info)
    pokemon_dict['types'] = get_types(pokemon_info)
    pokemon_dict['special_indicators'],pokemon_dict['prev_evo']  = get_special_indicators_prev_evo(pokemon_info)
    pokemon_dict['description'] = get_random_description(pokemon_info)
    pokemon_dict['damages'] = get_damages(pokemon_info)
    pokemon_dict['image'] = get_image_url(pokemon_info)
    #displaying the image
    #img = Image.open(urlopen(pokemon_dict['image']))
    #img = img.resize((200,200))
    #display(img)
    #img.show()
    #print(pokemon_dict)
    return pokemon_dict


