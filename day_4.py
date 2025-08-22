import random
user=int(input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors"))
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
if user>2:
    print("invalid input")

image = [rock,paper,scissors]
print(image[user])

print("Computer choose:")
computer=random.randint(0,2)
print(image[computer])

if user==1 and computer==0:
    print("you won")
elif user==2 and computer==1:
    print("you won")
elif user==0 and computer==2:
    print("you won")
elif user==0 and computer==1:
    print("you lose")
elif user==1 and computer==2:
    print("you lose")
elif user==2 and computer==0:
    print("you lose")
else:
    print("draw")
