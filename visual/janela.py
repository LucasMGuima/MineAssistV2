from utils import refs
from utils import functions as fun
import dearpygui.dearpygui as dpg

tg = refs.tags
lb = refs.labels

#Callbacks
def callback_addCord():
    resp = fun.adicionarCordenada()
    __atualizar_cords() if resp else print("Erro")

#janelas
def __window_config() -> None:
    pass

def __atualizar_cords() -> None:
    for item in dpg.get_item_children(tg.coordWindow)[1]:
        #Limpa a tabela
        dpg.delete_item(item)

    #Atualiza a tabela
    cords = fun.carregarCordenadas()
    for cord in cords:
        with dpg.table_row(parent=tg.coordWindow):
            dpg.add_text(cord[0])
            dpg.add_text(cord[1])
            dpg.add_text(cord[2])

    
#Janela principal
def creat_window(_width: int, _height: int) -> None:
    dpg.create_context()

    #Cria a janela
    with dpg.window(tag=tg.primareWindow):
        #Cria a barra de ferramentas
        with dpg.menu_bar():
            with dpg.menu(label=lb.save):
                dpg.add_menu_item(label=lb.trocar)
                dpg.add_menu_item(label=lb.novo)
                dpg.add_menu_item(label=lb.editar)
            #Configurações
            dpg.add_menu_item(label=lb.config, callback=__window_config)
        
        #Cria a coluna da tabela edição
        with dpg.group(horizontal=True, width=600):
            #Tabela
            with dpg.group():
                #-- Tabela de coordenadas
                with dpg.table(tag=tg.coordWindow, header_row=True, resizable=True,  policy=dpg.mvTable_SizingStretchProp,borders_outerH=True, borders_innerV=True, borders_innerH=True, borders_outerV=True):
                    dpg.add_table_column(label=lb.tb_col_nome)
                    dpg.add_table_column(label=lb.tb_col_overWord)
                    dpg.add_table_column(label=lb.tb_col_nether)
                    
                    cords = fun.carregarCordenadas()
                    for cord in cords:
                        with dpg.table_row():
                            dpg.add_text(cord[0])
                            dpg.add_text(cord[1])
                            dpg.add_text(cord[2])
        
            #Edição
            with dpg.child_window(label=lb.editCord, tag=tg.editWindow, autosize_x=True, autosize_y=True):
                with dpg.group():
                    dpg.add_text("--Editor--")
                    with dpg.group(horizontal=True):
                        dpg.add_text("Nome")
                        dpg.add_input_text(tag=tg.inpNome)
                    with dpg.group(horizontal=True):
                        dpg.add_text("Cord X:")
                        dpg.add_input_int(tag=tg.inpCordX, step=0)
                    with dpg.group(horizontal=True):
                        dpg.add_text("Cord Z:")
                        dpg.add_input_int(tag=tg.inpCordZ, step=0)
                dpg.add_button(label=lb.btn_adicionar, callback=callback_addCord)


    dpg.create_viewport(title="Mine Assistent", width=_width, height=_height)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window(tg.primareWindow, True)
    dpg.start_dearpygui()
    dpg.destroy_context()