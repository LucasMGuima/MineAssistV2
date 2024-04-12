import dearpygui.dearpygui as dpg

def adicionarCordenada() -> bool:
    """
        Adiciona uma nova coordenada.

        Return:
            True -> Salvo a nova coordenada.
            False -> Ocorreu algum erro.
    """
    from utils import refs as r

    nome = dpg.get_value(r.tags.inpNome)
    cord_x = int(dpg.get_value(r.tags.inpCordX))
    cord_z = int(dpg.get_value(r.tags.inpCordZ))

    if len(nome) <= 0: return False 
    
    try:
        __escreverCoordenada(nome, cord_x, cord_z)
        dpg.set_value(r.tags.inpNome, '')
        dpg.set_value(r.tags.inpCordX, 0)
        dpg.set_value(r.tags.inpCordZ, 0)
        return True
    except:
        return False


def __escreverCoordenada(nome:str, cord_x:int, cord_z:int, save:str = "teste") -> bool:
    import csv

    with open(f'./saves/{save}.csv', newline='\n', mode="+a") as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([nome, cord_x, cord_z])

def carregarCordenadas(save:str ="teste") -> list:
    """
        Carrega as coordenadas salvas no arquivo CSV.

        Return:
            lista contendo as coordenadas.
    """
    import csv

    cords = []

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

            