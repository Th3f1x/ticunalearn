import json


##############################################################################################
##############################################################################################
##############################################################################################
###1• To do: Colocar todas as palavras e expressões no dicionário para a devida tradução;#####
###2• To do: O programa ainda não possui uma função de edição (em caso de cometer erros)######
###########Para fazer edições edite diretamente no arquivo Json respeitando sua formatação.###
##############################################################################################
###################################################################Code Reviewer: th3f1x######
##############################################################################################

def load_dict(existent_file):
    try:
        with open(existent_file, 'r', encoding='UTF-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Dicionário JSON não encontrado.")
        return {}

def save_dict(dictionary, existent_file):
    with open(existent_file, 'w', encoding='UTF-8') as file:
        json.dump(dictionary, file, ensure_ascii=False, indent=4)

def add_to_dict(dictionary):
    while True:
        entry_type = input("Para adicionar uma palavra, digite (1), para uma expressão digite (2), para sair insira apenas dê enter.").strip().lower()

        if entry_type == '1':
            word = input("Digite a palavra na língua indígena: ").strip()
            translate = input(f"Digite a tradução da palavra '{word}' em português: ").strip()
            dictionary[word] = translate

        elif entry_type == '2':
            expression = input("Digite a expressão na língua indígena: ").strip()
            translate = input(f"Digite a tradução da expressão '{expression}' em português: ").strip()
            dictionary[expression] = translate


        else:
            print("Opção inválida. Finalizando aplicação . . .")
            break

    return dictionary

existent_file = 'ticuna.json' #Nome do dicionario json externo

dictionary = load_dict(existent_file)

dictionary = add_to_dict(dictionary)

save_dict(dictionary, existent_file)

print(f"dicionário salvo em '{existent_file}'.")
