def sexo(text):
   if text == 'male':
      text = 'Masculino'
   elif text == 'female':
      text = 'Feminino'
   else:
      text = text 
 
   return text

def cor_do_olho(text):
    if text == 'green':
        text = 'verde'
    elif text == 'blue':
        text = 'azul'
    elif text == 'red':
        text = 'vermelho'
    elif text == 'black':
        text = 'preto'
    elif text == 'brown':
        text = 'marrom'
    elif text == 'hazel':
        text = 'avelã'
    else:
        text = text
    return text


def cor_da_pele(text):
    if text == 'fair':
        text = 'clara'
    elif text == 'green':
       text = 'verde'
    elif text == 'dark':
        text = 'escura'
    elif text == "white, blue":
        text = "branco, azul"
    elif text == 'blue':
        text = 'azul'
   
    elif text == 'light':       
        text = 'clara'  
    
    

    else:
        text = text
    return text 


def tipo_terreno(text):
    if text == 'desert':
        text = 'deserto'
    elif text == 'jungle':
        text = 'selva'  
    elif text == 'forests':
        text = 'florestas'
    elif text == 'lakes':
        text = 'lagos'
    elif text == 'rivers':
        text = 'rios'
    elif text == "grassy hills, swamps, forests, mountains":
        text = 'colinas, pântanos, florestas, montanhas'
    else:
        text = text
    return text

def cor_do_cabelo(text):
    if text == 'white':
        text = 'branco'
    elif text == 'blond':
        text = 'loiro'
    elif text == 'brown':
        text = 'marrom'
    else:
        text = text
    return text