from enum import Enum


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
        self.reward = 0

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

        # self.environment = {
        #     (State.BOTTOM, Action.REST): (State.BOTTOM, 0.1),
        #     (State.BOTTOM, Action.CLIMB): (State.TOP, 0.0),
        #     (State.MIDDLE, Action.CLIMB): (State.TOP, 0.3),
        #     (State.MIDDLE, Action.DOWN): (State.BOTTOM, 1.0),
        #     (State.TOP, Action.REST): (State.TOP, 0.1),
        #     (State.TOP, Action.DOWN): (State.MIDDLE, 0.2),
        # }

    # def get_posible_actions(self, action):

    def move(self, action):
        # controla que la accion se pueda ejecutar en el estado actual
        if action in list(self.environment[self.state].keys()):
            print(True)
        else:
            print(False)
            # self.reward += self.environment[(State.BOTTOM, Action.REST)]
        # print(action in list(self.environment[self.state].keys()))


agent = Agent()
agent.move(Action.REST)
