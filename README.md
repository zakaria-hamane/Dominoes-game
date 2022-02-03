# Dominoes-game
Have you ever wanted to code a game where the computer is your enemy? Well, this little project allows you to do just that. Take turns playing classic dominoes against your computer in a race to victory. Learn, how artificial intelligence can make use of simple statistics to make educated decisions. This project is all about basic concepts, put them to practice by making a fun little game.

## I've written this game in python following this stages:

### 1- Setting up the game
Create and distribute the domino pieces between the players and the stock. Decide which player will make the first move.
### 2- The Interface
A good game should have a decent interface. Create a user-friendly output section.
### 3- Taking Turns
Bring the game to life. Allow players to take turns until the "end game" condition is met.
### 4- Enforcing Rules
A game should have rules. It's time to introduce them.
### 5- The AI
Random choices are hardly a sign of intelligence. Teach your computer to make educated decisions with the help of basic statistics.

## Exemple:
```
======================================================================
Stock size: 12
Computer pieces: 3

[4, 4][4, 2][2, 1][1, 0][0, 0][0, 2]

Your pieces:
1:[2, 2]
2:[3, 3]
3:[5, 5]
4:[6, 6]
5:[4, 5]
6:[3, 6]
7:[5, 6]

Status: Computer is about to make a move. Press Enter to continue...
>
======================================================================
Stock size: 12
Computer pieces: 2

[4, 4][4, 2][2, 1]...[0, 0][0, 2][2, 5]

Your pieces:
1:[2, 2]
2:[3, 3]
3:[5, 5]
4:[6, 6]
5:[4, 5]
6:[3, 6]
7:[5, 6]

Status: It's your turn to make a move. Enter your command.
>
```

```
======================================================================
Stock size: 12
Computer pieces: 3

[4, 4][4, 2][2, 1][1, 0][0, 0][0, 2]

Your pieces:
1:[2, 2]
2:[3, 3]
3:[5, 5]
4:[6, 6]
5:[4, 5]
6:[3, 6]
7:[5, 6]

Status: Computer is about to make a move. Press Enter to continue...
>
======================================================================
Stock size: 11
Computer pieces: 4

[4, 4][4, 2][2, 1][1, 0][0, 0][0, 2]

Your pieces:
1:[2, 2]
2:[3, 3]
3:[5, 5]
4:[6, 6]
5:[4, 5]
6:[3, 6]
7:[5, 6]

Status: It's your turn to make a move. Enter your command.
>
```
