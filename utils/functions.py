import dearpygui.dearpygui as dpg
from utils import refs as r
import csv

def adicionarCordenada() -> bool:
    """
        Adiciona uma nova coordenada.

        Return:
            True -> Salvo a nova coordenada.
            False -> Ocorreu algum erro.
    """

    nome = dpg.get_value(r.tags.inpNome)
    cord_x = int(dpg.get_value(r.tags.inpCordX))
    cord_z = int(dpg.get_value(r.tags.inpCordZ))

    if len(nome) <= 0: return False 
    
    try:
        if __escreverCoordenada(nome, cord_x, cord_z, dpg.get_value(r.tags.save)):
            dpg.set_value(r.tags.inpNome, '')
            dpg.set_value(r.tags.inpCordX, 0)
            dpg.set_value(r.tags.inpCordZ, 0)
            return True
        else:
            print('Erro Escrever Cord')
    except:
        return False

def atualizarCoordenada(save:str) -> bool:
    #Valores novos
    att_nome = dpg.get_value(r.tags.attNome)
    att_cordX = dpg.get_value(r.tags.attCordX)
    att_cordZ = dpg.get_value(r.tags.attCordZ)
    #Valores antigos
    old_val = dpg.get_value(r.tags.valorAntigo).split(',')
    old_nome = old_val[0]
    old_cordX = old_val[1]
    old_cordZ = old_val[2]

    try:
        with open(f'./saves/{save}.csv', newline='\n', mode='r') as file:
            reader = csv.reader(file, delimiter=',')
            att_linhas = []
            for linha in reader:
                if linha[0] == old_nome:
                    linha[0] = att_nome
                    linha[1] = att_cordX
                    linha[2] = att_cordZ
                att_linhas.append(linha)
            
        with open(f'./saves/{save}.csv', newline='\n', mode='w') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(att_linhas)
        
        #Limpa os campos
        dpg.set_value(r.tags.attNome, '')
        dpg.set_value(r.tags.valorAntigo, '')
        dpg.set_value(r.tags.attCordX, 0)
        dpg.set_value(r.tags.attCordZ, 0)

        return True
    except:
        return False

def __escreverCoordenada(nome:str, cord_x:int, cord_z:int, save:str) -> bool:
    print(save)
    with open(f'./saves/{save}.csv', newline='\n', mode="r") as file:
        reader = csv.reader(file, delimiter=',')
        for linha in reader:
            if linha[0] == nome: return False
    
    with open(f'./saves/{save}.csv', newline='\n', mode="a") as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([nome, cord_x, cord_z])
        return True

def carregarCordenadas(save:str) -> list:
    """
        Carrega as coordenadas salvas no arquivo CSV.

        Return:
            lista contendo as coordenadas.
    """
    cords = []
    try:
        with open(f'./saves/{save}.csv', newline='\n') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                nome = row[0]
                #OverWord Cord
                cord_x = row[1]
                cord_z = row[2]
                cord_o = f"X:{cord_x} Z:{cord_z}"
                #Nether Cord
                cord_nX = int(row[1])//8
                cord_nZ = int(row[2])//8
                cord_n = f"X:{cord_nX} Z:{cord_nZ}"

                new_cord = [nome, cord_o, cord_n]
                cords.append(new_cord)

        return cords
    except:
        return False

def listar_saves() -> list:
    from os import listdir

    saves = []
    for item in listdir('./saves'):
        save = item.split('.')[0]
        saves.append(save)
    return saves