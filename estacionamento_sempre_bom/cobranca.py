"""
O sistema deverá calcular o valor da cobrança,
saber a quantidade de veículos que estão no estacionamento por tipo,
saber o valor arrecadado até o momento e a quantidade de isentos.   

Critérios de cobrança do estacionamento Sempre Bom:
Até 15 minutos o cliente está isento de pagamento;
De 16 a 60 minutos é cobrado R$ 1,50;
Após 60 minutos de permanência é cobrado um adicional de R$ 1,00 por hora.
Os tipos de veículos aceitos no estacionamento são:
motocicletas, carros de passeio e camionetes. Os valores de cobrança são os mesmos para todos.
"""
from sempre_bom import Estacionamento

print('''Tabela de veículos aceitos:\nMotocicleta;\nCarro;\nCamionete.\n
Para Motocicleta digite: moto.\nPara Carro digite: carro.\nPara Camionete digite: camionete.\n''')
# Insere os dados do veículo
veiculo = input('Insira o tipo do veículo: ')
if veiculo == 'moto':
    print(f'Tipo de veículo: {veiculo}.')
else:
    print('Veículo invalido! Insira um veículo valido.')
# Insere os dados de tempo
tempo = int(input('Insira o tempo que o veículo utilizou o estacionamento: '))
if tempo > 60:
    valor = 2.5
    print(f'O veículo permaneceu um tempo de {tempo} minutos. O valor a ser pago é: R$ {valor}')
elif tempo > 16:
    valor = 1.5
    print(f'O veículo permaneceu um tempo de {tempo} minutos. O valor a ser pago é: R$ {valor}')
elif tempo <= 15:
    valor = 0.1
    print(f'O veículo permaneceu um tempo de {tempo} minutos. Veículo isento de pagamento.')
# Retorna os dados e os insere na tabela
if __name__ == "__main__":
    estacionamento = Estacionamento()
    estacionamento.insert(veiculo, tempo, valor)
