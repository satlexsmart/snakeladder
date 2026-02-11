from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from random import randint

class SnakeAndLadderGame(BoxLayout):
    def __init__(self, **kwargs):
        super(SnakeAndLadderGame, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.player_turn = 'Player 1'
        self.player1_position = 0
        self.player2_position = 0
        self.create_game_board()

    def create_game_board(self):
        self.game_board = Label(
            text='Welcome to Snake and Ladder Game',
            font_size=30
        )
        self.add_widget(self.game_board)

        self.player_turn_label = Label(
            text='Player Turn: ' + self.player_turn,
            font_size=20
        )
        self.add_widget(self.player_turn_label)

        self.roll_button = Button(
            text='Roll Dice',
            font_size=20
        )
        self.roll_button.bind(on_press=self.roll_dice)
        self.add_widget(self.roll_button)

        self.player1_position_label = Label(
            text='Player 1 Position: ' + str(self.player1_position),
            font_size=20
        )
        self.add_widget(self.player1_position_label)

        self.player2_position_label = Label(
            text='Player 2 Position: ' + str(self.player2_position),
            font_size=20
        )
        self.add_widget(self.player2_position_label)

    def roll_dice(self, instance):
        roll = randint(1, 6)
        if self.player_turn == 'Player 1':
            self.player1_position += roll
            if self.player1_position > 100:
                self.player1_position = 100
            if self.check_snake_or_ladder(self.player1_position):
                self.player1_position = self.check_snake_or_ladder(self.player1_position)
            self.player1_position_label.text = 'Player 1 Position: ' + str(self.player1_position)
            if self.player1_position == 100:
                self.game_board.text = 'Player 1 Wins'
                self.roll_button.disabled = True
            else:
                self.player_turn = 'Player 2'
                self.player_turn_label.text = 'Player Turn: ' + self.player_turn
        else:
            self.player2_position += roll
            if self.player2_position > 100:
                self.player2_position = 100
            if self.check_snake_or_ladder(self.player2_position):
                self.player2_position = self.check_snake_or_ladder(self.player2_position)
            self.player2_position_label.text = 'Player 2 Position: ' + str(self.player2_position)
            if self.player2_position == 100:
                self.game_board.text = 'Player 2 Wins'
                self.roll_button.disabled = True
            else:
                self.player_turn = 'Player 1'
                self.player_turn_label.text = 'Player Turn: ' + self.player_turn

    def check_snake_or_ladder(self, position):
        snakes = {
            17: 7,
            62: 19,
            64: 60,
            87: 24,
            93: 73,
            95: 75,
            98: 78
        }
        ladders = {
            1: 38,
            4: 14,
            9: 31,
            21: 42,
            28: 84,
            36: 44,
            51: 67,
            71: 91,
            80: 100
        }
        if position in snakes:
            self.game_board.text = 'Snake! Moving from ' + str(position) + ' to ' + str(snakes[position])
            return snakes[position]
        elif position in ladders:
            self.game_board.text = 'Ladder! Moving from ' + str(position) + ' to ' + str(ladders[position])
            return ladders[position]
        else:
            return None

class SnakeAndLadderApp(App):
    def build(self):
        return SnakeAndLadderGame()

if __name__ == '__main__':
    SnakeAndLadderApp().run()