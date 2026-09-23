class Restaurant:
    nome = ''
    categoria = ''
    ativo = False


restaurante_praca = Restaurant()
restaurante_praca.nome = 'Restaurante da Praça'
#Desafio 1
restaurante_praca.categoria = 'Italiana'

restaurante_pizza = Restaurant()
restaurante_pizza.nome = 'Restaurante da Pizza'
restaurante_pizza.categoria = 'Gourmet'

restaurantes = [restaurante_praca, restaurante_pizza]

print(vars(restaurantes[0]))
#Desafio 2
print(restaurantes[0].nome)

#Desafio 3
print('Restaurante da Praça está aberto') if restaurantes[0].ativo else print('Restaurante da Praça está fechado')

categoria_restaurante = Restaurant.categoria
print(f'A categoria do restaurante é: {categoria_restaurante}')

restaurante_praca.nome = 'Bistrô'

restaurante_pizza = Restaurant()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food.')
else:
    print('A categoria não é Fast Food.')

restaurante_pizza.ativo = True

print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')