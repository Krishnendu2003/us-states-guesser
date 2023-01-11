import turtle as t
import pandas
screen=t.Screen()
screen.title("U.S. States Game")
screen.setup(800,600)
img="blank_states_img.gif"
screen.addshape(img)
t.shape(img)

 # function to get the coordinates of states. outputs of this function are stored in the csv file already
# def get_coordinate_in_click(x,y):
#     print(x,y)
#
# t.onscreenclick(get_coordinate_in_click)
# t.mainloop()

data=pandas.read_csv("50_states.csv")
alll_states=data.state.to_list()
guessed_states=[]
while len(guessed_states)<50:

    answer_state=screen.textinput(title="Guess the states",prompt=f"{len(guessed_states)}/50 are correct").title()
     # if the answer state == one of the states in 50_states
     #     if they got right
     #        create a turtle to write the name of the states at thier respective coordinates
    if answer_state=="Exit":
        missing_state=[state for state in alll_states if state not in guessed_states]#list_comprehension
        # for state in alll_states:
        #     if state not in guessed_states:
        #         missing_state.append(state)
        missing_state_dataframe=pandas.DataFrame(missing_state)
        missing_state_dataframe.to_csv("States_to_learn.csv")
        break
    if answer_state in alll_states:
        guessed_states.append(answer_state)
        tim=t.Turtle()
        tim.hideturtle()
        tim.penup()
        states_data=data[data.state==answer_state]
        tim.goto(int(states_data.x),int(states_data.y))
        tim.write(answer_state)




screen.exitonclick()