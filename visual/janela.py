from utils import refs

import dearpygui.dearpygui as dpg

tg = refs.tags
lb = refs.labels

#janelas

def __window_config() -> None:
    pass

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
                dpg.add_text("--Coordenadas--")
                with dpg.table(header_row=True, resizable=True,  policy=dpg.mvTable_SizingStretchProp,borders_outerH=True, borders_innerV=True, borders_innerH=True, borders_outerV=True) as table:
                    dpg.add_table_column(label=lb.tb_col_nome)
                    dpg.add_table_column(label=lb.tb_col_overWord)
                    dpg.add_table_column(label=lb.tb_col_nether)
                    #TODO Chamar função de ler as coordenadas de dado arquivo
                    with dpg.table_row():
                        dpg.add_text("Vila")
                        dpg.add_text("X:80 Z:80")
                        dpg.add_text("X:10 Z:10")
        
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
                dpg.add_button(label=lb.btn_adicionar)


    dpg.create_viewport(title="Mine Assistent", width=_width, height=_height)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window(tg.primareWindow, True)
    dpg.start_dearpygui()
    dpg.destroy_context()