from utils import refs
from utils import functions as fun
import dearpygui.dearpygui as dpg

tg = refs.tags
lb = refs.labels

#Callbacks
def clb_addCord():
    resp = fun.adicionarCordenada()
    __atualizar_cords() if resp else print("Erro")

def clb_atualizar():
    resp = fun.atualizarCoordenada(dpg.get_value(tg.save))
    __atualizar_cords() if resp else print("Erro")

def clb_selecionavel(sender, app_data, user_data):
    nome = user_data[0]
    
    cord = user_data[1].split()
    cord_x = int(cord[0].split(":")[1])
    cord_z = int(cord[1].split(":")[1])

    dpg.set_value(tg.attNome, nome)
    dpg.set_value(tg.attCordX, cord_x)
    dpg.set_value(tg.attCordZ, cord_z)
    dpg.set_value(tg.valorAntigo, f"{nome},{cord_x},{cord_z}")

def clb_novoSave():
    fun.criarNovoSave()
    lst = __listar_saves()
    dpg.configure_item(tg.save, items=lst)
    dpg.configure_item(tg.novoSave, show=False)
#Janelas
def __window_config() -> None:
    pass

def __window_save() -> None:
    dpg.configure_item(tg.saveWindow, show=True)
    pass

def __novo_save() -> None:
    dpg.configure_item(tg.novoSave, show=True, pos=dpg.get_mouse_pos())
#Funcoes
def __remover_save() -> None:
    s_name = dpg.get_value(tg.save)
    fun.remover_save(s_name)
    lst = __listar_saves()
    dpg.configure_item(tg.save, items=lst)

def __atualizar_cords() -> None:
    for item in dpg.get_item_children(tg.coordWindow)[1]:
        #Limpa a tabela
        dpg.delete_item(item)

    #Atualiza a tabela
    cords = fun.carregarCordenadas(dpg.get_value(tg.save))
    if cords == False: return

    for cord in cords:
        with dpg.table_row(parent=tg.coordWindow):
            #Linha selecionavel
            dpg.add_selectable(label=f"{cord[0]}",callback=clb_selecionavel, user_data=(cord[0], cord[1]), span_columns=True)
            dpg.add_selectable(label=f"{cord[1]}",callback=clb_selecionavel, user_data=(cord[0], cord[1]), span_columns=True)
            dpg.add_selectable(label=f"{cord[2]}",callback=clb_selecionavel, user_data=(cord[0], cord[1]), span_columns=True)

def __listar_saves() -> list:
    resp = fun.listar_saves()
    return resp
#Janela principal
def creat_window(_width: int, _height: int) -> None:
    dpg.create_context()

    #Cria a janela
    with dpg.window(tag=tg.primareWindow):
        #Cria a barra de ferramentas
        with dpg.menu_bar():
            dpg.add_menu_item(label=lb.save, callback=__window_save)
            #Configurações
            dpg.add_menu_item(label=lb.config, callback=__window_config)
        
        #Cria a coluna da tabela edição
        with dpg.group(horizontal=True, width=600):
            #Tabela
            with dpg.group():
                #-- Tabela de coordenadas
                with dpg.table(tag=tg.coordWindow, header_row=True, resizable=False,borders_outerH=True, borders_innerV=True, borders_innerH=True, borders_outerV=True):
                    dpg.add_table_column(label=lb.tb_col_nome)
                    dpg.add_table_column(label=lb.tb_col_overWord)
                    dpg.add_table_column(label=lb.tb_col_nether)
                    
                    __atualizar_cords()
        
            #Edição
            with dpg.child_window(label=lb.editCord, tag=tg.editWindow, autosize_x=True, autosize_y=True):
                with dpg.group():
                    dpg.add_text("--Nova Coordenada--")
                    with dpg.group(horizontal=True):
                        dpg.add_text("Nome")
                        dpg.add_input_text(tag=tg.inpNome)
                    with dpg.group(horizontal=True):
                        dpg.add_text("Cord X:")
                        dpg.add_input_int(tag=tg.inpCordX, step=0)
                    with dpg.group(horizontal=True):
                        dpg.add_text("Cord Z:")
                        dpg.add_input_int(tag=tg.inpCordZ, step=0)
                    dpg.add_button(label=lb.btn_adicionar, callback=clb_addCord)
                with dpg.group():
                    dpg.add_text("--Editar Coordenada--")
                    #Salvar valores antigos
                    dpg.add_text(tag=tg.valorAntigo, show=False)
                    with dpg.group(horizontal=True):
                        dpg.add_text("Nome")
                        dpg.add_input_text(tag=tg.attNome)
                    with dpg.group(horizontal=True):
                        dpg.add_text("Cord X:")
                        dpg.add_input_int(tag=tg.attCordX, step=0)
                    with dpg.group(horizontal=True):
                        dpg.add_text("Cord Z:")
                        dpg.add_input_int(tag=tg.attCordZ, step=0)
                    dpg.add_button(label=lb.btn_atualizar, callback=clb_atualizar)    

    #Cria janela de PopUp
    #Saves
    with dpg.window(label=lb.save, tag=tg.saveWindow, show=False, width=200):
        with dpg.group(horizontal=True):
            dpg.add_text("Saves: ")
            lst_saves = __listar_saves()
            dpg.add_combo(items=lst_saves, tag=tg.save)
        with dpg.group(horizontal=True):
            dpg.add_button(label=lb.trocar, callback=__atualizar_cords)
            dpg.add_button(label=lb.novo, callback=__novo_save)
            dpg.add_button(label=lb.remover, callback=__remover_save)

    #Novo save
    with dpg.window(label=lb.novoSave, tag=tg.novoSave, show=False, width=200):
        with dpg.group(horizontal=True):
            dpg.add_text("Nome: ")
            dpg.add_input_text(tag=tg.novoSaveNome)
        with dpg.group(horizontal=True):
            dpg.add_button(label=lb.novo, callback=clb_novoSave)
            dpg.add_button(label=lb.cancelar)

    dpg.create_viewport(title="Mine Assistent", width=_width, height=_height)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window(tg.primareWindow, True)
    dpg.start_dearpygui()
    dpg.destroy_context()