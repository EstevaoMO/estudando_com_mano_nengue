from bichos.cachorro import Cachorro
from bichos.gato import Gato

def main():
    cachorro = Cachorro()
    gato = Gato()

    print(f"O nome do cachorro é {cachorro.nome} e sua raça é {cachorro.raca}")
    print(f"O nome do gato é {gato.nome} e sua raça é {gato.raca}")

    cachorro.latir()
    gato.miar()

if __name__ == "__main__":
    main()