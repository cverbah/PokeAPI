# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 14:25:39 2022

@author: c_ver
"""

from jinja2 import Environment
import webbrowser
from get_module import get_pokemon_info
from poke_validation import validate_pokemon

def render_html(data_pokemon):
    f = open('Pokedex.html', 'w')
    
    html_template = '''<!DOCTYPE html>
    <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="mystyle.css">
        </head>
    <body>
       
    <div class="column2">
    <div class="card">
    <h1># {{ id }} {{ name }} </h1>
       <img src={{ foto }} width="200" height="200">  
       <h3> Peso: {{ peso }} </h3>
       <h3> Estatura: {{ estatura }} </h3>
       <td><h5>Etapa previa: {{ evolu }}</h5></td>
    <div class="container">
    
        <h2>Estadísticas</h2>
        <table>
            <tr>
               <td><h5>HP: {{ hp }} </h5></td>
               <td><h5>Ataque: {{ ataque }}</h5></td>
               <td><h5>Defensa: {{ defensa }} </h5></td>
               <td><h5>Ataque Especial: {{ ataque_especial }} </h5></td>
               <td><h5>Defensa Especial: {{ defensa_especial }} </h5></td>
               <td><h5>Velocidad: {{ velocidad }} </h5></td>
            </tr>
        </table>
    <h3><b>Tipo</b></h3> 
  
        {% for elem in tipos %}
        <span class="label {{ dict_map[elem]}}">{{ elem }}</span>
        {% endfor %}</h5></td>
        {% for elem in tipos_special %}
        <span class="label other">{{ elem }}</span>
        {% endfor %}</h5></td>

    <p>{{ descripcion }}</p>

    <h3>Super efectivo contra:</h3>
            {% for elem in efectivo %}
            <span class="label {{ dict_map[elem]}}">{{ elem }}</span>
      
            {% endfor %}</h5></td>
                        
    <h3>Débil contra:</h3>
            {% for elem in debil %} 
            <span class="label {{ dict_map[elem]}}">{{ elem }}</span>
            {% endfor %}</h5></td>

    <h3>Resistente contra:</h3>
            {% for elem in resistente %} 
            <span class="label {{ dict_map[elem]}}">{{ elem }}</span>
            {% endfor %}</h5></td>
  
    <h3>Poco Eficaz contra:</h3>
            {% for elem in eficaz %} 
            <span class="label {{ dict_map[elem]}}">{{ elem }}</span>
            {% endfor %}</h5></td>
            
    <h3>Inmune contra:</h3>
            {% for elem in inmune %} 
            <span class="label {{ dict_map[elem]}}">{{ elem }}</span>
            {% endfor %}</h5></td>           
            
    <h3>Ineficaz contra:</h3>
             {% for elem in ineficaz %} 
             <span class="label {{ dict_map[elem]}}">{{ elem }}</span>
             {% endfor %}</h5></td>       
    
    </div>
    </div>
    </body>
    </html>'''
    ##mapping for style
    esp = ['Normal', 'Lucha', 'Volador', 'Veneno', 'Tierra', 'Roca', 'Bicho', 'Fantasma', 'Acero', 'Fuego',\
       'Agua', 'Planta', 'Eléctrico', 'Psíquico', 'Hielo', 'Dragón','Siniestro', 'Hada'] 

    eng = ['normal', 'fighting', 'flying', 'poison', 'ground', 'rock', 'bug', 'ghost', 'steel', 'fire',\
           'water','grass', 'electric', 'psychic', 'ice', 'dragon', 'dark', 'fairy']
        
    dict_map = {esp:eng for esp, eng in zip(esp,eng)}
    
    render_html = Environment().from_string(html_template)\
        .render(name = data_pokemon['name'], id = data_pokemon['id'], peso =data_pokemon['weight'],\
                estatura = data_pokemon['height'], foto = data_pokemon['image'],\
                evolu = data_pokemon['prev_evo'], hp = data_pokemon['stats']['PS'],\
                ataque = data_pokemon['stats']['Ataque'],defensa = data_pokemon['stats']['Defensa'],\
                ataque_especial = data_pokemon['stats']['Ataque Especial'],\
                defensa_especial = data_pokemon['stats']['Defensa Especial'] ,\
                velocidad = data_pokemon['stats']['Velocidad'],\
                tipos = data_pokemon['types'], descripcion = data_pokemon['description'],\
                efectivo = data_pokemon['damages']['double_damage_to'],\
                debil = data_pokemon['damages']['double_damage_from'],\
                resistente = data_pokemon['damages']['half_damage_from'], 
                eficaz = data_pokemon['damages']['half_damage_to'],\
                inmune = data_pokemon['damages']['no_damage_from'],\
                ineficaz = data_pokemon['damages']['no_damage_to'],\
                tipos_special = data_pokemon['special_indicators'],\
                dict_map = dict_map)          
                                          
    f.write(render_html)
    f.close()

def main():
    pokemon = validate_pokemon()
    data_pokemon = get_pokemon_info(pokemon)
    render_html(data_pokemon)
    webbrowser.open('Pokedex.html')
    
if __name__ == '__main__':
    main()