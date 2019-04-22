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


class Agent:

    def __init__(self):
        # estado inicial
        self.state = State.BOTTOM

        # recompenza acumulada
        self.accumulated_reward = 0

        # define el entorno (current state, action) => (next state, reward)
        self.environment = {
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

    for i in range(5):
        actions = agent.get_possible_action()
        random_action = int(np.random.rand() * 2)
        agent.move(actions[random_action])

random_agent()

agent = Agent()
print(agent.get_possible_action_reward())