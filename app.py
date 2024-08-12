import json


########################################################################################
########################################################################################
###1• To do: Implementar a função de tradutor;##########################################
###2• To do: Implementar função de formatação de texto;#################################
###3• To do: Implementar função de dump Json p/ projeto 2(Se o Ishikawa deixar? .-.);###
########################################################################################
###############################################################Code Reviewer: th3f1x####
########################################################################################



def load_dict(existent_file):
    try:
        with open(existent_file, 'r', encoding='UTF-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Dicionário JSON não encontrado.")
        return {}
    



existent_file = 'ticuna.json' #json dict 

dictionary = load_dict(existent_file)




















