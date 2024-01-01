import random

def play_game():
    options = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("Elige una opción (rock, paper, scissors): ").lower()

        if player_choice not in options:
            print("Opción no válida. Por favor, elige entre rock, paper o scissors.")
            continue

        computer_choice = random.choice(options)
        print(f"El oponente eligió: {computer_choice}")

        if player_choice == computer_choice:
            print("Empate!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'scissors' and computer_choice == 'paper') or \
             (player_choice == 'paper' and computer_choice == 'rock'):
            print("¡Ganaste!")
            player_score += 1
        else:
            print("Perdiste.")
            computer_score += 1

        play_again = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if play_again != 's':
            break

    print(f"Puntuación final: Jugador {player_score} - {computer_score} Oponente")

play_game()

