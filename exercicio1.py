#receber a idade do usuário como inteiro numa varíavel
var_idade = int(input("Digite sua idade: "))
# Testa se a idade é menor ou igual a 16 nos
if var_idade >= 16:
  # Se é maior ou igual (verdade True )
  # mostre a mensagem abaixo no terminal 
    print('Oba! você já pode votar...')
else: 
    # Se é menor (mentira false)
    print('oops1 Você ainda não pode votar...')