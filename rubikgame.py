from play_details import Player
from tabulate import tabulate


def view_menu_details():
    """
    display navigation
    :return:
    """
    print('\n---- enter your key to continue ----\n')
    print(tabulate([['Start the game-->', 1], ['Check the winner-->', 2], ['Exit from the game-->', -1]], headers=['Instruction', 'Key']))


def start_game():
    """
    to retrieve the name of the player
    :return: player reference
    """
    print('\nenter your name : ', end=' ')
    name = input()
    p = Player(name)
    return p


def menu_result_board():
    """
    display result navigation
    :return:
    """
    print('To view your own results of 3 rounds --> type 1 and enter : ', end=' ')


if __name__ == '__main__':
    player_count = 0

    while True:
        view_menu_details()
        print('\nEnter your instruction number from above list : ', end=' ')
        input_instruction = input()
        if int(input_instruction) == 1:
            player = start_game()
            print('\n---PLAYER '+str(player_count)+'---\n')
            player_count += 1
            print('To start playing the game --> type 1 and enter : ', end=' ')
            play_status = input()
            if int(play_status)==1:
                for i in range(1, 4):
                    print('\nstart lucky draw round '+str(i))
                    play_details = player.play()
                print('\n3 lucky rounds are finished\n')
                menu_result_board()
                result_status = input()
                if int(result_status) == 1:
                    player.view_round_results()
                elif int(result_status) == 2:
                    player.get_match_results()
        elif int(input_instruction) == -1:
            print('\nThank you for playing')
            break
        elif int(input_instruction) == 2:
            print("\n\nThe winner of the game is : "+Player.get_match_results(player))
            break





