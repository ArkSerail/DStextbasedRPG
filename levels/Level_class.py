import sys
import time

class Level():

    def __init__(self, level_text, decision_text, options):
        self.level_text = level_text
        self.decision_text = decision_text
        self.options = options
        self.option_text = ""
    
    def level_start(self):
        for char in self.level_text:
            sys.stdout.write(char)
            sys.stdout.flush()

            time.sleep(0.01)
        input("")

    def level_decision(self):
        print(self.decision_text)
        print(self.option_text)    

    def define_decision_text(self):
        text = "Optionen: "
        for element in self.options:
            text += f"[{element}] "
        
        self.option_text = text
        