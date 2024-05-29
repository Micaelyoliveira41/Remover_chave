pessoa= {
    'Nome': 'Micaely Oliveira',
    'Idade': 24,
    'Profissão': 'Tec Enfermagem',
    'Empresa': 'Hospitalar',
    'Gênero': 'Feminino',
    'Cidade': 'Planaltina'
}
# remover chave
del pessoa[input('informe o nome da chave a ser deletada: ')]

for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')