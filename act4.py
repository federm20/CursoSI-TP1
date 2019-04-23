from enum import Enum
import numpy as np


# posibles estados del agente
class State(Enum):
    BOTTOM = 1
    MIDDLE = 2
    TOP = 3


# posibles acciones a efectuar por el agente
class Action(Enum):
    REST = 1
    CLIMB = 2
    DOWN = 3


# definición del entorno
class Environment:

    def __init__(self):
        # define el entorno (current state) => [(action) => (next state, reward)]
        self.definition = {
            State.BOTTOM: {
                Action.REST: (State.BOTTOM, 0.1),
                Action.CLIMB: (State.TOP, 0.0)
            },
            State.MIDDLE: {
                Action.CLIMB: (State.TOP, 0.3),
                Action.DOWN: (State.BOTTOM, 1.0)
            },
            State.TOP: {
                Action.REST: (State.TOP, 0.1),
                Action.DOWN: (State.MIDDLE, 0.2)
            }
        }


# definición del agente
class Agent:

    def __init__(self):
        # estado inicial
        self.state = State.BOTTOM

        # recompenza acumulada
        self.accumulated_reward = 0

        # factor de descuento
        self.gamma = 0.2

        # define el ambiente donde se desarrolla el agnete
        self.environment = Environment().definition

        # muestra el estado actual
        print("Estado inicial: BOTTOM")
        print("Recompenza acumulada: 0")

    # función que retorna las posibles acciones del estado actual
    def get_possible_action(self):
        return list(self.environment[self.state].keys())

    # función que retorna las posibles acciones del estado actual y la recompenza de cada una
    def get_possible_action_reward(self):
        return list(self.environment[self.state].items())

    # función que permite al agente moverse en un entorno definido (realizar una accion según su estado actual)
    def move(self, action):
        # controla que la accion se pueda ejecutar en el estado actual
        if action in list(self.environment[self.state].keys()):
            self.accumulated_reward += self.environment[self.state][action][1]
            self.state = self.environment[self.state][action][0]

            print("Acción: {}".format(action))
            print("Estado: {}".format(self.state))
            print("Recompenza acumulada: %.2f" % self.accumulated_reward)
        else:
            print("Movimiento no permitido - Existe un error")


def random_agent():
    # crea el agente
    agent = Agent()

    for i in range(50):
        actions = agent.get_possible_action()
        random_action = int(np.random.rand() * 2)
        agent.move(actions[random_action])


# considera que el agente tiene dos acciones disponibles en cada estado
def e_random_agent(e):
    # crea el agente
    agent = Agent()

    for i in range(5):
        # obtiene acciones posibles
        actions = agent.get_possible_action_reward()

        random = np.random.rand()

        # obtiene la accion con minima recompenza
        if actions[0][1][1] < actions[1][1][1]:
            min_reward = 0
        else:
            min_reward = 1

        agent.move(actions[random_action])


# random_agent()
e_random_agent(0.2)
