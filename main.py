import requests

def main():
    print('####################')
    print('### Quiz sobre programação ###')
    print('####################')
    print()

    request = requests.get('https://raw.githubusercontent.com/joseluiz123/GamePro/main/pergunta1.json')

    address_data = request.json()
    #print(request)

    if 'erro' not in address_data:

        print('Pergunta: {}'.format(address_data['pergunta']))

        resposta = input("Digite a resposta: ")
        resposta_correta = address_data['resposta_correta']

        if resposta == resposta_correta:
            print("Parabéns vc acertou!")
        else:
            print("Resposta errada")

    else:
        print('Desculpe, aconteceu algum erro, tente executar novamente.')

    print('---------------------------------')

if __name__ == '__main__':
    main()
