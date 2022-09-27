# Linguagens Formais e Automatos 🎓

O trabalho prático consiste na implementação de um programa que permita cadastrar e testar autômatos finitos. A solução deve permitir que o usuário cadastre seu próprio autômato finito determinístico, não-determinístico ou não-determinístico com transições vazias, indicando os estados, as transições e valores do alfabeto. Após o cadastro deve ser possível testar se uma determinada palavra faz parte ou não da linguagem representada pelo autômato.

## Linguagem Utilizada 💻
- `Python` 🐍
- [Código online no Replit](https://replit.com/@rendmp/Linguagens-Formais-e-Aut-matos-Trabalho-Pr-tico-1#main.py)

## Componentes do grupo
- Pedro Felipe Barbosa Rodrigues

## Como utilizar
Edite o arquivo input.txt com o automato escrito da forma correta (o script não irá analisar reportar errors caso ocorra erro de sintaxe) e execute o código no shell:
	python main.py

Estados: [s0, s1]
Estado Inicial: [s0, None]
Estado de aceitação: ['s1']
Alfabeto: ['a', 'b']
Transições: ['s0:a>s0', 's0:b>s1']

Digite uma palavra: ab

Estado atual após as transições: s1