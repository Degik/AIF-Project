import gym
import numpy as np
import minihack
import matplotlib.pyplot as plt
import IPython.display as display
# Costruisco l'ambienete con il comando make e lo ritorno nella variabile env
env = gym.make("MiniHack-ExploreMaze-Easy-Mapped-v0")
# Prendo lo stato mediante reset nella variabile state
state = env.reset()
# Disegno l'ambiente
env.render()
