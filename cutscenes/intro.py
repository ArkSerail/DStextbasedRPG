####### Functions & schleifen
import time
import sys


def intro():
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



    
    for char in intro_text:
        sys.stdout.write(char)
        sys.stdout.flush()

        time.sleep(0.01)



if __name__ == "__main__":
    intro()