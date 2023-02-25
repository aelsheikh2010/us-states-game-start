import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
guessing_list = []
while len(guessing_list) < 50:
    answer_state = screen.textinput(title=f"{len(guessing_list)}/50 states correct",
                                    prompt="what's another state name?: ").title()
    if answer_state == "Exit":
        difference_list = []
        for element in all_state:
            if element not in guessing_list:
                difference_list.append(element)
        df = pandas.DataFrame(difference_list)
        df.to_csv("states_to_learn.csv")
        new_data = pandas.read_csv("states_to_learn.csv")
        print(new_data)
        break
    if answer_state in all_state:
        guessing_list.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# states_to_learn.csv






