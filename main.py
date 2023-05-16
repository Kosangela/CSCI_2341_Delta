import random
from hangman_art import logo, stages
from hangman_words import word_list

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

print("Welcome to the games menu!")
game_choice = input("Enter 1 to play Hangman, or 2 to play Rock-Paper-Scissors: ")

if game_choice == "1":
  chosen_word = random.choice(word_list)
  word_length = len(chosen_word)
  end_of_game = False
  lives = 6

  print(logo)

  #Create blanks
  display = []
  for _ in range(word_length):
      display += "_"

  while not end_of_game:
      guess = input("Guess a letter: ").lower()

      if guess in display:
          print(f"You guessed the same word before {guess}")
      #Check guessed letter
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter

      #Check if user is wrong.
      if guess not in chosen_word:
          if guess not in chosen_word:
              print("Your guess "+guess+" is not true give us another guess.")
          lives -= 1
          if lives == 0:
              end_of_game = True
              print("You lose.")

      print(f"{' '.join(display)}")

      #Check if user has got all letters.
      if "_" not in display:
          end_of_game = True
          print("You win.")

      print(stages[lives])

elif game_choice == "2":
  print("Welcome to the rock, paper, scissors game!")
  your_choice = input("What do you choose? 0 for rock, 1 for paper or 2 for scissors.\n")
  your_choice_int = int(your_choice)

  if your_choice_int == 0:
      print(rock)
  elif your_choice_int == 1:
      print(paper)
  elif your_choice_int == 2:
      print(scissors)

  print("Computer chose:\n")
  computer_choice = random.randint(0, 1)

  if computer_choice == 0:
      print(rock)
  elif computer_choice == 1:
      print(paper)
  elif computer_choice == 2:
      print(scissors)

  if your_choice_int == 0 and computer_choice == 0:
      print("It's a draw!")
  elif your_choice_int == 1 and computer_choice == 1:
      print("It's a draw!")
  elif your_choice_int == 2 and computer_choice == 2:
      print("It's a draw!")
  elif your_choice_int == 0 and computer_choice == 1:
      print("You loose!")
  elif your_choice_int == 1 and computer_choice == 2:
      print("You loose!")
  elif your_choice_int == 2 and computer_choice == 0:
      print("You loose!")
  else:
      print("You won!")
else:
  print("Invalid choice. Please enter 1 or 2.")