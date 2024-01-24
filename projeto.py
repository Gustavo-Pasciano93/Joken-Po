import random
import sys


pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

imagens_jogo = [pedra, papel, tesoura]

escolha_do_usuario = int(input( "O que você escolhe? Aperte 0 para Pedra, 1 para Papel e 2 para Tesoura. \n"))


if escolha_do_usuario >= 3 or escolha_do_usuario < 0:
    print("Você digitou um número inválido, você perdeu!")
    sys.exit() 
else:
    print(imagens_jogo [escolha_do_usuario])

escolha_computador = random.randint(0,2)
print("O computador escolheu:")
print(imagens_jogo [escolha_computador] )


if escolha_do_usuario ==0 and escolha_computador == 2:
    print("Você ganhou!!!")
elif  escolha_computador == 0 and escolha_do_usuario == 2:
    print(" Você perdeu !!!")    
elif escolha_computador > escolha_do_usuario:
    print("Você perdeu!!")
elif escolha_do_usuario > escolha_computador:
    print("Você ganhou!!!!")
elif escolha_computador == escolha_do_usuario:
    print("Temos um empate")
        