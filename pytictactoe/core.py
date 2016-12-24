class Player:
    def __init__(self, player_type, symbol):
        self.player_type = player_type
        self.symbol = symbol

    def play(self, current_state):
        if self.player_type == "human":
            print(current_state)
            action = None
        elif self.player_type == "random":
            action = 

        return action

class Game:
    def isFinal(self, state):
        is_final = False

        # Check if there is at least one empty square
        if state.count(0) == 0:
            is_final = True

        # Check lines
        elif abs(sum(state[0:3]))==3 or abs(sum(state[3:6]))==3 or abs(sum(state[6:9]))==3:
            is_final = True

        # Check columns
        elif abs(sum(state[0:9:3]))==3 or abs(sum(state[1:9:3]))==3 or abs(sum(state[2:9:3]))==3:
            is_final = True

        # Check diagonals
        elif abs(sum(state[0:9:4]))==3 or abs(sum(state[2:7:2]))==3:
            is_final = True

        return is_final

    def nextState(self, current_state, action)
        return 0

    def status(self, current_state):
        return "draw"


game = Game()

player_list = [Player("human", "X"), Player("random", "O")]
current_player_index = 0
current_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]

while not game.isFinial():
    current_player = player_list[current_player_index]
    action = current_player.play(current_state)
    current_state = game.nextState(current_state, action)
    current_player_index = (current_player_index + 1) % 2

print(current_state)     # Optionnal, should be moved in player.play for human players only
print(game.status(current_state))
