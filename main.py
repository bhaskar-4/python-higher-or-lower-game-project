import random
from art import logo,vs
from game_data import data

def assign():
    return random.choice(data)
def points_updation(points):
    return points+1



def print_details(x):
    print(x["name"]+", a "+x["description"]+", From "+x["country"])

def switch(x,y):
    global score
    x.clear()  # Clears the existing dictionary in place
    x.update(y)  # Copies all key-value pairs from y into x

    y.clear()  # Clears the second dictionary
    y.update(assign())  # Assigns a new dictionary to y
    score = points_updation(score)



def comparison(x,y):
    global score

    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_choice=='a' and x["follower_count"]>y["follower_count"] or user_choice=='b' and x["follower_count"]<y["follower_count"]:
        switch(x, y)
        print("\n"*50)
        print(f"You're right! Current score: {score}.")
        return True

    else:
        print("\n" * 50)
        print(f"Sorry, that's wrong. Final score: {score}")
        return False




def play():
    global a,b,score
    print(logo)
    while True:
        print("Compare A: ",end='')
        print_details(a)
        print(vs)
        print("Against B: ",end='')
        print_details(b)
        if not comparison(a, b):
            break

a=assign()
b=assign()
while a==b:
    b=assign()
score=0

play()