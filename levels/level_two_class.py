from levels.Level_class import Level
#from Level_class import Level


def level_two():
    level_text = r"""    Während du durch die düsteren Gänge der Burg wanderst, begegnen dir groteske Kreaturen und untote Soldaten,

    die deinen Weg blockieren....
    """

    decision_text = r""" An der Wand neben dir hängt ein altes rostiges Schwert
    
    Möchtest du es nehmen?"""

    possible_answers = ['Ja', 'Nein']

    level = Level(level_text, decision_text, possible_answers)

    level.define_decision_text()
    level.level_start()
    level.level_decision()
    user_input = ""
    while user_input not in possible_answers:
        user_input = input()
        if user_input == "Ja":
            print("Du hast das Schwert aufgehoben!")
            print("Mit dem Schwert in der Hand kannst du die Kreaturen vor dir bekämpfen und deinen Weg weiter aus der Burg hinaus vorangehen.")
        elif user_input == "Nein":
            print("Ohne das Schwert wirst du von den Kreaturen vor dir überwältigt.")
            level.defeat_screen()
        else:
            print("Bitte gib eine gültige Antwort ein")


            


if __name__ == "__main__":
     level_two()