from minihack import LevelGenerator

def createLevel(width:int = 20, height:int = 20, monster:str = "goblin", weapon:str="tsurugi"):
    level_generated = LevelGenerator(w = width, h=height)
    level_generated.add_object("apple", symbol="%")
    level_generated.add_object(name=weapon, symbol=")")
    #level_generated.add_object(')', (7, 7))  # Aggiungi un'arma
    #level_generated.add_object('*', (9, 9))  # Aggiungi un oggetto
    #level_generated.add_monster(name=monster)
    #level_generated.add_sink()
    return level_generated.get_des()

