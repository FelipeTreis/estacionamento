"""Sistema para buscar registros."""
from sempre_bom import Estacionamento


if __name__ == "__main__":
    estacionamento = Estacionamento()
    print(estacionamento.search(input('Insira um id: '), type_s="id"))
    print('veículo/tempo em minutos/valor/id')