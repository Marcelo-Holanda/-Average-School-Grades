
nota1 = float(input('Primeira Nota:'))
nota2 = float(input('Segunda Nota:'))
nota3 = float(input('Terceira Nota:'))
media = (nota3 + nota2 + nota1) / 3


if media < 5:
    print('A Média alcançada foi {:.2f}'.format(media))
    print('SITUAÇÃO: REPROVADO')
elif media >= 5 and media < 7:
     print('A média alcançada foi {:.2f}'.format(media))
     print('SITUAÇÃO: EM RECUPERAÇÃO.')
elif media >= 7:
    print('A média alcançada foi {}'.format(media))
    print('SITUAÇÃO: APROVADO.')








