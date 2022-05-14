'''Sistema para buscar registros.'''
from sempre_bom import Estacionamento


if __name__ == "__main__":
    estacionamento = Estacionamento()
    print(estacionamento.search(input('Insira o tipo de veículo: '), type_s="veiculo"))