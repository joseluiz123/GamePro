import requests



def main():
    print('##############################')
    print('### Quiz sobre programação ###')
    print('##############################')
    print()
    pontos = 0
    request = requests.get('https://raw.githubusercontent.com/joseluiz123/GamePro/main/pergunta1.json')

    address_data = request.json()
    #print(request)

    if 'erro' not in address_data:

        for i in range(1,3):
            pergunta = address_data[f'pergunta{i}']
            #print('Pergunta: {}'.format(address_data['pergunta']))
            print(f'Pergunta {i}: ' + pergunta)

            resposta = input("Digite a resposta: ")
            resposta_correta = address_data[f'resposta_correta{i}']

            if resposta == resposta_correta:
                print("Parabéns vc acertou!")
                pontos = pontos + 10
            else:
                print("Resposta errada")
            print('===================')
        print(f'Você conseguiu fazer: {pontos}')

    else:
        print('Desculpe, aconteceu algum erro, tente executar novamente.')

    print('---------------------------------')

if __name__ == '__main__':
    main()

'''Um desenvolvedor implementou um programa para exibir a média de um dado retirado de uma grande base de dados. Para isso, foi utilizada a linguagem Python. O trecho do código que mostra o resultado é apresentado a seguir. Assinale a alternativa correta acerca desse trecho de código sabendo que a média do usuário foi 75.

print('Sua média foi {}.'.format(med))

A O programa imprime: Sua média foi 75.
B O programa imprime: Sua média foi {}.
C O programa imprime: Sua média foi Null.
D O programa apresenta um erro na impressão porque tenta converter tipo numérico em caractere.
E O programa apresenta um erro na impressão, pois não apresenta o formato do valor.'''
