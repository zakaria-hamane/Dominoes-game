import random
from collections import Counter
import operator


def dominoSet():
    return [[i, j] for i in range(7) for j in range(i, 7)]


def doubleDominoList(domino_set):
    return [domino for domino in domino_set if domino[0] == domino[1]]


def shuffleDominoSet(domino_set):
    random.shuffle(domino_set)
    return domino_set


def splitDominoSet(shuffled_set):
    return shuffled_set[:7], shuffled_set[7:14], shuffled_set[14:]


def checkDouble(players, spinners):
    return any((i in players) for i in spinners)


def dominoSnakeBase(first_player, spinners):
    return max(i for i in spinners if i in first_player)


def nestedtoList(domino_set):
    return [i for domino in domino_set for i in domino]


def sortDict(domino_scores):
    sorted_keys = sorted(domino_scores, key=domino_scores.get)
    return {w: domino_scores[w] for w in sorted_keys}


def checkStatus(player, computer, spinners):
    if checkDouble(player, spinners) is True and checkDouble(computer, spinners) is False:
        return "computer"
    elif checkDouble(computer, spinners) is True and checkDouble(player, spinners) is False:
        return "player"
    elif checkDouble(player, spinners) is True and checkDouble(computer, spinners) is True:
        return (
            "computer"
            if dominoSnakeBase(player, spinners) > dominoSnakeBase(computer, spinners)
            else "player"
        )
    else:
        return "Reshuffle"


def otherPlayer(status):
    players = ["player", "computer"]
    for player in players:
        if player == status:
            continue
        return player


def yourPieces(player):
    print("Your pieces:")
    print("\n".join(f'{player.index(i) + 1}:{i}' for i in player))


def checkSymbol(user_input):
    return user_input < 0


def dominoSnakePrinter(domino_snake):
    if len(domino_snake) <= 6:
        print("".join(f'{i}' for i in domino_snake))
    else:
        first = "".join(f'{i}' for i in domino_snake[:3])
        last = "".join(f'{i}' for i in domino_snake[-3:])
        print(f'{first}...{last}')


def playerMove(player_command, status, stock_pieces):
    if player_command != 0:
        return eval(status).pop(abs(player_command) - 1)
    else:
        return stock_pieces.pop(random.randint(0, len(stock_pieces) - 1))


def checkEndGame(domino_snake):
    if domino_snake[0][0] == domino_snake[len(domino_snake) - 1][1]:
        item_list = [item for sublist in domino_snake for item in sublist]
        return item_list.count(5) >= 8


def interfacePrinter(player, computer, stock_pieces, status, domino_snake):
    print("=" * 70)
    print("Stock size:", len(stock_pieces))
    print("Computer pieces:", len(computer))
    print("")
    dominoSnakePrinter(domino_snake)
    print("")
    yourPieces(player)
    print("")
    if status == "player":
        print("Status:",
              "It's your turn to make a move. Enter your command.")
    elif status == "computer":
        print("Status:",
              "Computer is about to make a move. Press Enter to continue...")
    elif status == "End of game" and len(player) == 0:
        print("Status:",
              "The game is over. You won!")
    elif status == "End of game" and len(computer) == 0:
        print("Status:",
              "The game is over. The computer won!")
    elif status == "Draw":
        print("Status:",
              "The game is over. It's a draw!")


def calcNumScores(computer, domino_snake):
    computer_list = nestedtoList(computer)
    domino_snake_list = nestedtoList(domino_snake)
    return dict(Counter(computer_list + domino_snake_list))


def calcDominoScores(computer, num_scores):
    domino_scores = {}
    for index, domino in enumerate(computer, 1):
        score_head = num_scores[domino[0]] if domino[0] in num_scores.keys() else 0
        score_tail = num_scores[domino[1]] if domino[1] in num_scores.keys() else 0
        domino_scores[index] = score_head + score_tail
    return domino_scores


def sortDict(domino_scores):
    sorted_tuple = sorted(domino_scores.items(), key=lambda x:x[1])
    sorted_commands = []
    for k, v in sorted_tuple:
        sorted_commands.append(k)
    return sorted_commands


def compCommandScores(comp_commands, domino_scores):
    comp_commands_scores = {}
    for k, v in domino_scores.items():
        for i in comp_commands:
            if abs(i) == k:
                comp_commands_scores[i] = v
    return comp_commands_scores


def compCommand(sorted_commands):
    comp_command = [sorted_commands[len(sorted_commands) - 1] if sorted_commands else 0]
    if comp_command != 0 and len(sorted_commands) > 1:
        if abs(sorted_commands[len(sorted_commands) - 2]) == sorted_commands[len(sorted_commands) - 1]:
            comp_command.append(sorted_commands[len(sorted_commands) - 2])
    return comp_command\


def ComputerAI(computer, domino_snake):
    num_scores = calcNumScores(computer, domino_snake)
    domino_scores = calcDominoScores(computer, num_scores)

    verify_list = []
    comp_commands = []
    for domino in computer:
        if domino[0] == domino_snake[0][0] or domino[1] == domino_snake[0][0]:
            verify_list.append(True)
            comp_commands.insert(0, -computer.index(domino) - 1)
        if domino[0] == domino_snake[len(domino_snake) - 1][1] or domino[1] == domino_snake[len(domino_snake) - 1][1]:
            verify_list.append(True)
            comp_commands.append(computer.index(domino) + 1)
        else:
            verify_list.append(False)
    
    comp_commands_scores = compCommandScores(comp_commands, domino_scores)
    sorted_commands = sortDict(comp_commands_scores)
    comp_command = compCommand(sorted_commands)
    return verify_list, comp_command


class IllegalMoveError(Exception):
    pass


def playersCommand(status, computer, domino_snake):
    global verify_list, comp_command
    verify_list, comp_command = ComputerAI(computer, domino_snake)
    while True:
        try:
            player_input = input()
            if status == "computer":
                player_command = random.choice(comp_command) #if any(verify_list) else 0
            elif status == "player":
                player_command = int(player_input)
            if player_command > len(eval(status)) or player_command < -len(eval(status)):
                raise IndexError
            elif player_command != 0:
                if checkSymbol(player_command):
                    if domino_snake[0][0] not in eval(status)[abs(player_command) - 1]:
                        raise IllegalMoveError('Illegal move. Please try again..')
                elif not checkSymbol(player_command):
                    if domino_snake[len(domino_snake) - 1][1] not in eval(status)[abs(player_command) - 1]:
                        raise IllegalMoveError('Illegal move. Please try again..')
            return player_command

        except IndexError:
            print("Invalid input. Please try again.")
        except IllegalMoveError as im:
            if status == "player":
                print(im)


def gameStart():
    while True:
        domino_snake = []
        domino_set = dominoSet()
        spinners = doubleDominoList(domino_set)
        shuffled_set = shuffleDominoSet(domino_set)
        player, computer, stock_pieces = splitDominoSet(shuffled_set)
        status = checkStatus(player, computer, spinners)

        # append domino snake base
        first_player_set = eval(otherPlayer(status))
        domino_snake_base = first_player_set.pop(
            first_player_set.index(
                dominoSnakeBase(first_player_set, spinners)
            )
        )
        domino_snake.append(domino_snake_base)

        if status != "Reshuffle":
            interfacePrinter(player, computer, stock_pieces, status, domino_snake)
            break
    return status, domino_snake, player, computer, stock_pieces


def gameRunner(player_command, status, domino_snake, stock_pieces, player, computer):
    if player_command == 0:
        player_move = playerMove(player_command, status, stock_pieces)
        eval(status).append(player_move)
        status = otherPlayer(status)
    elif checkSymbol(player_command):
        player_move = playerMove(player_command, status, stock_pieces)
        if player_move[0] == domino_snake[0][0]:
            player_move.reverse()
        domino_snake.insert(0, player_move)
        status = otherPlayer(status)
    elif not checkSymbol(player_command):
        player_move = playerMove(player_command, status, stock_pieces)
        if player_move[1] == domino_snake[len(domino_snake) - 1][1]:
            player_move.reverse()
        domino_snake.append(player_move)
        status = otherPlayer(status)
    return status, domino_snake, player, computer, stock_pieces


def main():
    global status, domino_snake, player, computer, stock_pieces
    status, domino_snake, player, computer, stock_pieces = gameStart()
    while len(player) != 0 and len(computer) != 0:
        player_command = playersCommand(status, computer, domino_snake)
        if status in ["player", "computer"]:
            if player_command == 0 and domino_snake == 0:
                continue
            else:
                status, domino_snake, player, computer, stock_pieces = gameRunner(player_command, status, domino_snake,
                                                                                  stock_pieces, player, computer)
                interfacePrinter(player, computer, stock_pieces, status, domino_snake)

        elif (
            status != "player"
            and status != "computer"
            and checkEndGame(domino_snake)
        ):
            # If the numbers on the ends of the snake are identical and appear within the snake 8 times
            status = "Draw"
            interfacePrinter(player, computer, stock_pieces, status, domino_snake)
    status = "End of game"
    interfacePrinter(player, computer, stock_pieces, status, domino_snake)


if __name__ == "__main__":
    main()
