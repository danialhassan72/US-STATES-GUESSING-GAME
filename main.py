import turtle
import pandas as pd

class USStatesGame:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("U.S. States Game")
        self.screen.addshape("blank_states_img.gif")
        turtle.shape("blank_states_img.gif")

        self.data = pd.read_csv("50_states.csv")
        self.all_states = self.data["state"].tolist()
        self.guessed_states = []

    def get_state_data(self, state_name):
        return self.data[self.data.state == state_name]

    def display_state_name(self, state_data, state_name):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_name)

    def play_game(self):
        first_prompt = True
        while len(self.guessed_states) < 50:
            if first_prompt:
                answer_state = self.screen.textinput(
                    title="Guess the state name",
                    prompt="Guess the state name"
                ).title()
                first_prompt = False
            else:
                answer_state = self.screen.textinput(
                    title=f"{len(self.guessed_states)}/50 States Correct",
                    prompt="What's another state's name? Type 'Exit' to end the game."
                ).title()

            if answer_state == "Exit":
                break

            if answer_state in self.all_states and answer_state not in self.guessed_states:
                self.guessed_states.append(answer_state)
                state_data = self.get_state_data(answer_state)
                self.display_state_name(state_data, answer_state)

        self.save_results()
        self.screen.bye()  # Close the turtle graphics window

    def save_results(self):
        missing_states = [state for state in self.all_states if state not in self.guessed_states]
        missing_data = pd.DataFrame(missing_states, columns=["state"])
        missing_data.to_csv("states_to_learn.csv", index=False)

        guessed_data = pd.DataFrame(self.guessed_states, columns=["state"])
        guessed_data.to_csv("guessed_states.csv", index=False)

if __name__ == "__main__":
    game = USStatesGame()
    game.play_game()
