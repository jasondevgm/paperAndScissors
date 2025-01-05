import inquirer
import os
import time

# Define the Player class
class Player:
    def __init__(self, name, colour, score=0):
        self.name = name
        self.colour = colour
        self.score = score

    def greeting(self):
        print(f"Hola me llamo {self.name}")

# Define the choices for inquirer prompts
colour_choice = [
    inquirer.List('Choice', message="  Selecciona tu color",
                  choices=['\033[1;34;40m Azul', '\033[1;31;40m Rojo', '\033[1;36;40m Cyan'])
]

hand_choice = [
    inquirer.List('Choice', message="  Selecciona piedra, papel o tijera",
                  choices=['Piedra', 'Tijeras', 'Papel'])
]

continue_game = [
    inquirer.List('Choice', message="  Quieres continuar?",
                  choices=['Continuar', 'Salir'])
]

def create_player(name, colour):
    """Create a new player with the given name and colour."""
    return Player(name, colour)

def get_colour_from_choice(choice):
    """Return the colour code based on the choice."""
    if choice["Choice"] == '\033[1;34;40m Azul':
        return '\033[1;34;40m'
    elif choice["Choice"] == '\033[1;31;40m Rojo':
        return '\033[1;31;40m'
    else:
        return '\033[1;36;40m'

def get_hand_number_from_choice(choice):
    """Convert hand choice to a corresponding number."""
    if choice["Choice"] == "Piedra":
        return 1
    elif choice["Choice"] == "Tijeras":
        return 2
    elif choice["Choice"] == "Papel":
        return 3

def display_final_victory(player1, player2):
    """Display the final victory screen."""
    os.system("cls")
    print("  Partida de piedra, papel o tijera")
    print("#####################################################\n\n")
    print("\t Fin de la partida\n")
    print("\tJugador 1")
    print(f"\t   Nombre: {player1.name}")
    print(f"\t   Puntos: {player1.score}")
    print("\tJugador 2")
    print(f"\t   Nombre: {player2.name}")
    print(f"\t   Puntos: {player2.score}")
    print("\n\n##################################")

def play_game_round(player1, player2):
    """Play a single round of the game."""
    normal_colour = '\033[0m'

    def player_turn(player, opponent):
        os.system("cls")
        print(player.colour, "Partida de piedra, papel o tijera")
        print("#####################################################\n")
        print(f"\tTurno de \"{player.name}\" jugador\n", normal_colour)
        print(f"  Que {opponent.colour}{opponent.name}{normal_colour} no mire mientras {player.colour}{player.name}{normal_colour} escoje una de las manos\n")
        time.sleep(1)
        answer = inquirer.prompt(hand_choice)
        return get_hand_number_from_choice(answer), answer["Choice"]

    hand_player1, choice1 = player_turn(player1, player2)
    hand_player2, choice2 = player_turn(player2, player1)

    print(f"  Mano jugador uno \"{choice1}\" mano jugador dos \"{choice2}\"")

    # Determine the winner of the round
    if hand_player1 == hand_player2:
        print("  empate")
    elif (hand_player1 == 1 and hand_player2 == 2) or (hand_player1 == 2 and hand_player2 == 3) or (hand_player1 == 3 and hand_player2 == 1):
        print(f"  Gana {player1.colour}{player1.name}{normal_colour} jugador 1")
        player1.score += 1
    else:
        print(f"  Gana {player2.colour}{player2.name}{normal_colour} jugador 2")
        player2.score += 1

    print("\n#####################################################")
    print("\n\tJugador 1")
    print(f"\t   Nombre: {player1.name}")
    print(f"\t   Puntos: {player1.score}")
    print("\tJugador 2")
    print(f"\t   Nombre: {player2.name}")
    print(f"\t   Puntos: {player2.score}")
    print("\n\n#####################################################\n")
    continue_game_table = inquirer.prompt(continue_game)

    if player1.score == 2 or player2.score == 2:
        display_final_victory(player1, player2)
    else:
        if continue_game_table["Choice"] == "Continuar":
            play_game_round(player1, player2)

def main():
    """Main function to start the game."""
    os.system("cls")
    print("  Partida de piedra, papel o tijera")
    print("  #####################################################")

    print("\nDefinicion de los jugadores\n")

    def define_player(player_number):
        print(f"\tJugador {player_number}")
        player_name = input("____________Nombre del jugador: ")
        player_colour = get_colour_from_choice(inquirer.prompt(colour_choice))
        return create_player(player_name, player_colour)

    player1 = define_player(1)
    os.system("cls")
    print("Partida de piedra, papel o tijera")
    print("#####################################################")
    print("\nDefinicion de los jugadores\n")
    player2 = define_player(2)

    # Start the game
    play_game_round(player1, player2)

main()