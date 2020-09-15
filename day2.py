space= "\n"
print("Welcome to my First Game!")

name= input("What is your name? ")
age= input("What is your age? ")


health = 10



if age >= "18":
    wants_to_play= input("Radical, do you want to play? ").lower()

    if wants_to_play == "Yes" or "yes":
        print("You are starting with", health, "heatlh.")
        print(space)
        print("Let's play! ")

        left_or_right = input("First choice... Left of Right? ").lower()
        if left_or_right == "left":
            ans = input("Nice, you followed the path and reach a lake... Do you swim across or go around? ").lower()

            if ans== "around":
                print("You went around and reached the other end of the lake.")

            if ans== "across":
                print("You somehow made it across but, a shark bit you along the way and you lost 5 health...")
                health-= 5

        if left_or_right == "right":
            ans= input("Ouch, you fell a died...")

        else:
            print("You lost...")
    else:
     print("Cya...")

elif age >="13":
    print("You can play with supervision. ")
else:
    print("You are not old enough to play...")





gviuvy



'''
string "hello", "hi", "89"
int 8, 7, -9, 10000
float 6.0, 7.5, -9.8, -100.0
bool True, False
'''
