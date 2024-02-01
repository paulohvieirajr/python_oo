from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
# restaurante_mexicano = Restaurante('Mexican Food', 'Maxicana')
# restaurante_japones = Restaurante('Japa', 'Japonesa')
# restaurante_mexicano.alternar_estado()
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()