import random
print('rock(r),paper(p),scissor(s)?')
player1 = input()
print('you choose: ', player1)
if player1 == 'r':
    print('Rock : o ')
elif player1 == 'p':
    print('Paper : ___')
elif player1 == 's':
    print('Scissor : >8')

com = random.randint(1,3)
if com == 1:
    player2 = 'r'
elif com == 2:
    player2 = 'p'
else : player2 = 's'
print('computer choosed :', player2)
print('THE GAME IS ',player1,' vs ',player2)

if player1 == player2:
    print('Its a DRAW')
elif player1 == 'r' and player2 == 'p':
    print("Player2 Won")
elif player1 == 'r' and player2 == 's':
    print("Player1 Won")
elif player1 == 'p' and player2 == 'r':
    print("Player1 Won")
elif player1 == 'p' and player2 == 's':
    print("Player2 Won")
elif player1 == 's' and player2 == 'r':
    print("Player2 Won")
elif player1 == 's' and player2 == 'p':
    print("Player1 Won")