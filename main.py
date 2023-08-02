import turtle
import pandas

screen = turtle.Screen()
screen.title("India State Game")
image = "gifgit.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("india-states.csv")
all_states = data.State.to_list()

guessed_state = []

while len(guessed_state) < 31:


    answer_state = screen.textinput(title=f"{len(guessed_state)}/31 State Correct", prompt="What's another State Name?").title()

    if answer_state == "Exit":
        # missing_state = []
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_state.append(state)

        # Using List comprehension method
        missing_state = [state for state in all_states if state not in guessed_state]

        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("States_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_location = data[data.State == answer_state]
        t.goto(int(state_location.x), int(state_location.y))
        t.write(answer_state)

turtle.mainloop()
