from levels.Level_class import Level


def level_one():
    level_text = r"""    Du erwachst in einer düsteren und verlassenen Welt namens Lordran, ohne Erinnerungen an deine Vergangenheit oder deinen Zweck. 
    
    Du spürst, dass eine wichtige Aufgabe auf dich wartet....
    """

    decision_text = r""" Du schaust dich um und findest dich wieder in einer Zelle. 
    
    Vor dir liegt etwas funkelndes...
    
    Aufheben?"""

    possible_answers = ['Ja', 'Nein']

    level = Level(level_text, decision_text, possible_answers)

    level.define_decision_text()
    level.level_start()
    level.level_decision()
    user_input = ""
    while user_input not in possible_answers:
        user_input = input()
        if user_input == "Ja":
            print("Du hast einen Schlüssel aufgehoben!")
            print("Mit dem Schlüssel öffnest du die Tür vor dir, du findest dich in einem dunklen gang einer alten, zerstörten Burg wieder")
        elif user_input == "Nein":
            print("Du hast den Gegenstand nicht aufgehoben. Du siehst jedoch, dass es ein Schlüssel ist, die Tür vor dir scheint verschlossen zu sein.")
            pick_up_key()
        else:
            print("Bitte gib eine gültige Antwort ein")


def pick_up_key():
    text = r""" Willst du den Schlüssel aufheben?"""
    print(text)
    print("Optionen: [Ja] - [Nein]")
    possible_answers = ['Ja', 'Nein']
    user_input = ""
    while user_input not in possible_answers:
        user_input = input()
        if user_input == "Ja":
            print("Du hast den Schlüssel aufgehoben!")
        else:
            print("Ohne den Schlüssel scheinst du nicht weiter zu kommen. Willst du ihn aufheben?")
            


if __name__ == "__main__":
     level_one()