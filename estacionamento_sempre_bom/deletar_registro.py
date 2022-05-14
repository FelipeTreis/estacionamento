'''Sistema para deletar registros.'''
from sempre_bom import Estacionamento


if __name__ == "__main__":
    estacionamento = Estacionamento()
    estacionamento.delete("moto")