from colorama import Fore 
from bardapi import Bard

token = 'cggHpA-0e_zBNi2OQTUexf4Q_I7Z6ZIbpoeKueNnhoKFFtXHtwbl9atQNt_NbRO9D91Mlg.'

def get_response(text):
    bard = Bard(token=token)
    response = bard.get_answer("puede corregirme este output que posee errores de mi ocr? \n: ",text)['content']
    response_fore = (response.split("**")[1].split("**")[0])
    response = (f"{Fore.GREEN}{response_fore}")
    return response



