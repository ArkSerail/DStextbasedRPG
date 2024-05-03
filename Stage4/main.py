import platform
import os
import sys
import time
### Resources
CHARACTER_NAME = ""
start_picture = r"""
                                                                                                 ⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣯⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⢺⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⣧⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⣿⣋⣟⠭⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣭⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⢮⣳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡿⣦⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠢⣽⣅⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆⢤⣿⡇⠀⠀⠀⠀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠸⣞⡇⠀⠀⠀⠀⡏⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⣿⣷⠀⠀⠀⠀⢻⡈⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⢸⣿⡆⠀⠀⠀⠀⢳⣬⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡈⣿⣧⠀⠀⢠⡄⣸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⢹⣿⡀⠀⢸⢧⠟⢹⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠸⣿⡇⣠⠋⢾⣾⢸⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡖⠀⠸⣿⣶⣿⣷⡏⢰⡿⢿⠏⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⣴⢋⣿⣿⣿⠇⡟⠁⣏⠀⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡞⣏⢦⠇⢸⡿⢿⠋⢀⣤⣀⡘⢦⡟⢸⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⠃⢀⣴⡆⠀⠀⠈⣹⣿⡷⠆⠀⣧⠈⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠜⢁⡴⠋⡀⠙⢄⠀⣰⣿⣟⠓⠀⠀⢉⣴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⢰⡏⡠⠊⢀⡴⣇⠀⢀⡞⠉⠛⠀⡀⢀⣄⣩⠌⠙⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⢣⠶⠖⠊⢀⣈⠉⣹⡷⢀⣴⡯⠔⣛⡵⠁⣠⡏⠸⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⢹⡿⢿⠟⠀⣰⡞⠉⣿⡷⠇⠃⣠⢴⣶⣾⡋⢀⡴⣽⠁⠀⠘⣏⣀⢰⣆⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⣠⣶⣶⣅⣠⣶⠀⠒⠟⢁⡴⠋⠀⠀⠀⢹⣿⣿⡋⣧⢸⡇⡏⣀⣀⠀⠙⣿⣉⠙⢤⡄⠀⠀⠀
                                                                                        ⠀⠀⣠⣴⣺⢿⣿⣿⡛⠛⠿⠿⣯⣷⡲⣶⣟⣻⡀⠀⣠⣿⣿⣖⣸⣨⣿⠿⠛⣻⣿⣶⣾⣾⠇⠀⠻⣄⠀⠀
                                                                                        ⠀⣾⢟⠿⠿⢶⣮⡙⢏⢢⡀⢠⡌⣿⣿⡿⠟⡿⢳⣼⣿⣿⣿⣾⣿⣧⣤⣤⣤⣿⣿⣭⣿⠁⠀⠀⣀⣈⣧⠀
                                                                                        ⢺⣥⢿⠾⠿⠿⠿⡿⠚⢋⣠⠯⣿⢉⢉⠻⠾⠛⢿⣿⠻⠿⢛⢋⣤⣯⣭⠽⠶⣾⣻⢿⣻⢿⠶⢛⣻⡿⢽⠄"""

start_game_dialog=r"""

████████▄     ▄████████    ▄████████    ▄█   ▄█▄         ▄████████  ▄██████▄  ███    █▄   ▄█          ▄████████          ███        ▄████████ ▀████    ▐████▀     ███        ▄████████    ▄███████▄    ▄██████▄  
███   ▀███   ███    ███   ███    ███   ███ ▄███▀        ███    ███ ███    ███ ███    ███ ███         ███    ███      ▀█████████▄   ███    ███   ███▌   ████▀  ▀█████████▄   ███    ███   ███    ███   ███    ███ 
███    ███   ███    ███   ███    ███   ███▐██▀          ███    █▀  ███    ███ ███    ███ ███         ███    █▀          ▀███▀▀██   ███    █▀     ███  ▐███       ▀███▀▀██   ███    ███   ███    ███   ███    █▀  
███    ███   ███    ███  ▄███▄▄▄▄██▀  ▄█████▀           ███        ███    ███ ███    ███ ███         ███                 ███   ▀  ▄███▄▄▄        ▀███▄███▀        ███   ▀  ▄███▄▄▄▄██▀   ███    ███  ▄███        
███    ███ ▀███████████ ▀▀███▀▀▀▀▀   ▀▀█████▄         ▀███████████ ███    ███ ███    ███ ███       ▀███████████          ███     ▀▀███▀▀▀        ████▀██▄         ███     ▀▀███▀▀▀▀▀   ▀█████████▀  ▀▀███ ████▄  
███    ███   ███    ███ ▀███████████   ███▐██▄                 ███ ███    ███ ███    ███ ███                ███          ███       ███    █▄    ▐███  ▀███        ███     ▀███████████   ███          ███    ███ 
███   ▄███   ███    ███   ███    ███   ███ ▀███▄         ▄█    ███ ███    ███ ███    ███ ███▌    ▄    ▄█    ███          ███       ███    ███  ▄███     ███▄      ███       ███    ███   ███          ███    ███ 
████████▀    ███    █▀    ███    ███   ███   ▀█▀       ▄████████▀   ▀██████▀  ████████▀  █████▄▄██  ▄████████▀          ▄████▀     ██████████ ████       ███▄    ▄████▀     ███    ███  ▄████▀        ████████▀  
                          ███    ███   ▀                                                 ▀                                                                                  ███    ███                           
"""

end_game = r"""
                                                                                ▄██   ▄    ▄██████▄  ███    █▄        ▄█     █▄   ▄█  ███▄▄▄▄   
                                                                                ███   ██▄ ███    ███ ███    ███      ███     ███ ███  ███▀▀▀██▄ 
                                                                                ███▄▄▄███ ███    ███ ███    ███      ███     ███ ███▌ ███   ███ 
                                                                                ▀▀▀▀▀▀███ ███    ███ ███    ███      ███     ███ ███▌ ███   ███ 
                                                                                ▄██   ███ ███    ███ ███    ███      ███     ███ ███▌ ███   ███ 
                                                                                ███   ███ ███    ███ ███    ███      ███     ███ ███  ███   ███ 
                                                                                ███   ███ ███    ███ ███    ███      ███ ▄█▄ ███ ███  ███   ███ 
                                                                                 ▀█████▀   ▀██████▀  ████████▀        ▀███▀███▀  █▀    ▀█   █▀  

"""

### Start Screen / Menu
def start_game():
    print(start_picture)
    print(start_game_dialog)
    print("\n \n                                                                                                           Press any key to start! \n\n")
    input("")

#### Erstelle Charakter
def charakter_erstellung():
    character_ascii = r"""
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⢤⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⡟⠛⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⣀⣠⠞⢹⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⣶⣆⣐⢿⣿⠃⣈⣰⣄⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⡌⣿⠟⡱⣾⣞⡙⣼⣿⣆⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣬⡿⠿⢾⢿⣿⣿⢻⢻⡯⣿⣂⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢻⣧⡧⡡⢺⠸⣿⣷⡦⠽⢻⡄⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣾⣿⣎⠇⡄⣄⣼⣿⣦⣔⠈⢻⡴⣶⡀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿⣾⣿⣿⡓⠴⠿⠿⠿⣿⣿⡿⢋⠈⢸⣧⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⣏⠧⣿⣿⣿⣟⠻⡛⠛⢋⣿⠟⠔⠁⠀⢨⣿⡀
                        ⠀⠀⠀⠀⠀⠀⠀⠰⢦⣽⣿⢧⢩⡟⠶⣟⣋⡽⢣⠊⠀⠀⠀⢸⡿⡇
                        ⠀⠀⠀⠀⠀⠀⠀⣲⣷⣿⣿⣿⣿⣾⡇⣲⡿⢡⠃⠀⠀⠀⠀⢸⢻⡇
                        ⠀⠀⠀⢠⣀⡠⡺⠋⢹⣧⣝⣿⢇⣿⣷⡿⠁⠆⠀⠀⠀⠀⠀⢺⣿⡇
                        ⠀⠀⠄⣁⠟⢏⠀⠀⣼⡿⠻⢾⣼⣿⢿⠇⣸⠀⠀⠀⠀⠀⢐⣿⣿⠇
                        ⡍⣠⠞⠁⠄⠁⠰⣶⢿⣯⣀⣾⡿⠁⠚⠀⢥⣭⣁⠂⢀⠀⣎⡽⡻⠀
                        ⠚⣁⠤⠴⠀⠀⣼⠹⢹⡾⠛⡏⠀⠀⠀⠀⠀⠹⣿⣿⣦⢳⠕⣀⣀⣀
                        ⠉⠀⠀⠀⠀⠐⡙⠶⠾⢷⣽⠀⠀⠀⠀⠀⠀⠀⣣⣭⣿⠟⡄⠉⠉⠉


"""
    print(character_ascii)
    print("Gib dem Helden einen Namen")
    charakter_name()
    get_charakter_name()
    input("")

### Intro
def intro():

    intro_bild = r"""
                                        ___________________________________________________
                                        @@@@@@@@@@@@@@@@@@@@@**^^""~~~"^@@^*@*@@**@@@@@@@@@
                                        @@@@@@@@@@@@@*^^'"~   , - ' '; ,@@b. '  -e@@@@@@@@@
                                        @@@@@@@@*^"~      . '     . ' ,@@@@(  e@*@@@@@@@@@@
                                        @@@@@^~         .       .   ' @@@@@@, ~^@@@@@@@@@@@
                                        @@@~ ,e**@@*e,  ,e**e, .    ' '@@@@@@e,  "*@@@@@'^@
                                        @',e@@@@@@@@@@ e@@@@@@       ' '*@@@@@@    @@@'   0
                                        @@@@@@@@@@@@@@@@@@@@@',e,     ;  ~^*^'    ;^~   ' 0
                                        @@@@@@@@@@@@@@@^""^@@e@@@   .'           ,'   .'  @
                                        @@@@@@@@@@@@@@'    '@@@@@ '         ,  ,e'  .    ;@
                                        @@@@@@@@@@@@@' ,&&,  ^@*'     ,  .  i^"@e, ,e@e  @@
                                        @@@@@@@@@@@@' ,@@@@,          ;  ,& !,,@@@e@@@@ e@@
                                        @@@@@,~*@@*' ,@@@@@@e,   ',   e^~^@,   ~'@@@@@@,@@@
                                        @@@@@@, ~" ,e@@@@@@@@@*e*@*  ,@e  @@""@e,,@@@@@@@@@
                                        @@@@@@@@ee@@@@@@@@@@@@@@@" ,e@' ,e@' e@@@@@@@@@@@@@
                                        @@@@@@@@@@@@@@@@@@@@@@@@" ,@" ,e@@e,,@@@@@@@@@@@@@@
                                        @@@@@@@@@@@@@@@@@@@@@@@~ ,@@@,,0@@@@@@@@@@@@@@@@@@@
                                        @@@@@@@@@@@@@@@@@@@@@@@@,,@@@@@@@@@@@@@@@@@@@@@@@@@
                                        ___________________________________________________

"""

    intro_text = r"""    Zur Zeit der Alten war die Welt ungeformt und in Nebel gehüllt. Ein Land grauer Felsen und ewiger Drachen. Doch dann kam das Feuer, und mit dem Feuer kam das Ungleiche. 
    
    Hitze und Kälte, Leben und Tod und natürlich Licht und Finsternis. 

    Dann kamen sie aus der Finsternis und fanden die Seelen der Herren in den Flammen. Nito, der Erste der Toten, die Hexe von Izalith und ihre Töchter des Chaos, Gwyn, der Herr des Sonnenlichts und seine treuen Ritter. 

    Und der Pelzige Pygmäe, den man so leicht vergisst.

    Mit der Macht der Fürsten forderten sie die Drachen heraus. Gwyns mächtige Blitze zerschmetterten ihre steinernen Schuppen. 

    Die Hexen woben gewaltige Feuerstürme. Nito entfesselte ein Miasma von Tod und Krankheit, Seath der Skalblose verriet die Seinen, und die Drachen waren nicht mehr.

    So begann das Zeitalter des Feuers. Doch bald werden die Flammen erlöschen und nur die Finsternis wird bleiben. Schon jetzt gibt es nur Glut, und die Menschen sehen kein Licht, sondern nur endlose Nächte. 

    Und unter den Lebenden sieht man Träger des verfluchten dunklen Zeichens.

    Das dunkle Zeichen kennzeichnet die Untoten. 

    Und in diesem Land werden die Untoten zusammengetrieben und nach Norden geführt, wo sie eingesperrt werden, um auf das Ende der Welt zu warten...

    Das ist dein Schicksal.
    
    """
    print(intro_bild)
    animate_text(intro_text)
    input("")
#### Outro
def outro():
    print(end_game)
    input("")

def defeat_screen():
        ascii_code = r"""
                                    ▄██   ▄    ▄██████▄  ███    █▄        ▄█        ▄██████▄     ▄████████     ███     
                                    ███   ██▄ ███    ███ ███    ███      ███       ███    ███   ███    ███ ▀█████████▄ 
                                    ███▄▄▄███ ███    ███ ███    ███      ███       ███    ███   ███    █▀     ▀███▀▀██ 
                                    ▀▀▀▀▀▀███ ███    ███ ███    ███      ███       ███    ███   ███            ███   ▀ 
                                    ▄██   ███ ███    ███ ███    ███      ███       ███    ███ ▀███████████     ███     
                                    ███   ███ ███    ███ ███    ███      ███       ███    ███          ███     ███     
                                    ███   ███ ███    ███ ███    ███      ███▌    ▄ ███    ███    ▄█    ███     ███     
                                     ▀█████▀   ▀██████▀  ████████▀       █████▄▄██  ▀██████▀   ▄████████▀     ▄████▀   
                                                                         ▀                                             """
        print(ascii_code)

### Clear screen
def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    if platform.system() == "Linux":
        os.system('clear')

def animate_text(text):
    i = 0
    while i < len(text):
        sys.stdout.write(text[i])
        sys.stdout.flush()
        time.sleep(0.01)
        i=i+1

def charakter_name():
    name = input("")
    global CHARACTER_NAME 
    CHARACTER_NAME = name

def get_charakter_name():
    print(f"Du bist der Held: {CHARACTER_NAME}")
    return CHARACTER_NAME

def level_one():
    text = r"""    Du erwachst in einer düsteren und verlassenen Welt namens Lordran, ohne Erinnerungen an deine Vergangenheit oder deinen Zweck. 
    
    Du spürst, dass eine wichtige Aufgabe auf dich wartet....
    """

    animate_text(text)
    print("")
    print("")
    text = r"""    Du schaust dich um und findest dich wieder in einer Zelle. 
    
    Vor dir liegt etwas funkelndes...
    
    Aufheben?
    Optionen: [Ja] - [Nein]"""
    animate_text(text)

    user_input = ""
    while user_input != 'Ja':
        user_input = input()
        if user_input == "Ja":
            print("Du hast einen Schlüssel aufgehoben!")
            print("Mit dem Schlüssel öffnest du die Tür vor dir, du findest dich in einem dunklen gang einer alten, zerstörten Burg wieder")
        elif user_input == "Nein":
            print("Du hast den Gegenstand nicht aufgehoben. Du siehst jedoch, dass es ein Schlüssel ist, die Tür vor dir scheint verschlossen zu sein.")
            print("Möchtest du den Schlüssel aufheben? \n Optionen: [Ja] - [Nein]")
        else:
            print("Bitte gib eine gültige Antwort ein")

def level_two():
    feuerball_ascii = r"""


                                ⠀⠀⠀⠀⠀⠀⢠⣤⡄⠀⠀⠀⠀⠀⠀⠀⠠⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⢀⣀⣀⣈⠉⠁⠀⣀⣀⡀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⢸⣿⠇⣿⣧⠀⢸⣿⣿⣧⠀⠀⠀⠀⠀⣿⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⡀⠀⣠⣿⣿⣦⣈⣻⣿⠏⢰⣶⠀⠀⣰⡟⠉⠙⠻⢶⣄⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠈⠛⠛⠉⣾⠏⠉⠉⠁⠀⢀⣁⣤⡾⠋⠀⠀⠀⠀⠀⠻⣧⠀⠀⠀⠀⠀
                                ⠀⡀⠀⠀⠀⣀⡼⢿⣄⠀⠀⠀⠀⠀⢹⣧⠀⣠⣶⣶⣦⣄⠀⠀⣿⠀⠀⠀⠀⠀
                                ⠀⠛⠛⠛⠛⠋⠀⠀⢹⣆⠀⠈⠻⠾⠿⠋⠀⠻⣿⡿⠀⢻⡇⠀⣿⡀⠀⠀⠀⠀
                                ⠀⣤⣄⠀⢰⣿⣿⣷⣸⡟⠀⣾⣦⣤⡀⠀⢠⣤⡀⠀⠀⣼⣧⡀⢻⡇⠀⠀⠀⠀
                                ⠀⠀⠙⣷⡈⠻⠿⠿⠛⠁⢀⣿⠿⢿⣿⠀⠈⠉⠀⠐⣾⠋⠛⠃⠈⣿⡀⠀⠀⠀
                                ⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⢸⡇⠀⠘⠋⠀⢠⣤⣤⣤⣿⣿⣷⣦⢀⣿⣿⣄⠀⠀
                                ⠀⠀⠀⠀⠘⢷⣤⣀⠀⠀⠸⣇⠀⠀⠀⠀⠈⠉⠉⠻⣿⣿⣿⣧⣾⣿⣿⣿⡆⠀
                                ⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠛⠻⣆⠀⠀⢀⣾⣿⣿⡆⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠉⠁⠀⠀⠀
                                
    """
    level_text_1 = r"""    Während du durch die düsteren Gänge der Burg wanderst, begegnen dir groteske Kreaturen und untote Soldaten,

    die deinen Weg blockieren.... auf ein Mal kommt ein FEUERBALL!!!"""

    level_text_2 = r"""
    auf dich zugeflogen! dem du gerade noch ausweichen kannst.
    """
    level_text = level_text_1 + feuerball_ascii + level_text_2
    animate_text(level_text)
    print("\n")
    print("\n")
    decision_text = r""" An der Wand neben dir hängt ein altes rostiges Schwert
    
    Möchtest du es nehmen?
    Optionen: [Ja] - [Nein]"""

    animate_text(decision_text)
    print("\n")
    user_input = ""
    while user_input != "Ja" and user_input != "Nein":
        user_input = input()
        if user_input == "Ja":
            print("Du hast das Schwert aufgehoben!")
            print("Mit dem Schwert in der Hand kannst du die Kreaturen vor dir bekämpfen und deinen Weg weiter aus der Burg hinaus vorangehen.")
            outro()
        elif user_input == "Nein":
            print("Ohne das Schwert wirst du von den Kreaturen vor dir überwältigt.")
            defeat_screen()
        else:
            print("Bitte gib eine gültige Antwort ein")

if __name__ == "__main__":
    try:
        start_game()
        clear_screen()
        charakter_erstellung()
        clear_screen()
        intro()
        clear_screen()
        level_one()
        clear_screen()
        level_two()
    except BaseException as exp:
        print("Das Spiel wurde vom Spieler beendet!")
        sys.exit(0)
