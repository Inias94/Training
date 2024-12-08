import turtle
import csv
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
guessed_states = []
states_to_learn = []
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
print(all_states)
score = 0

while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(title=f"{score}/{len(all_states)} Guess the state",
                                    prompt="What's another state name?").title()

    if answer_state == "Exit":
        states_to_learn = [states for states in guessed_states if states not in guessed_states]
        # for states in all_states:
        #     if states not in guessed_states:
        #         states_to_learn.append(states)
        pandas.DataFrame(states_to_learn).to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        score += 1
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)


