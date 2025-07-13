# 1040 - Média 3

n1, n2, n3, n4 = map(float, input().split())

media = (2*n1 + 3*n2 + 4*n3 + n4)/10
print(f'Media: {round(media, 1)}')

if media >= 7:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
elif media >= 5 and media < 6.9:
    print('Aluno em exame.')
    nf = float(input())
    print(f'Nota do exame: {round(nf, 1)}')
    nova_media = (media + nf)/2
    if nova_media >= 5:
        print('Aluno aprovado.')
    else: 
        print('Aluno reprovado.')
    print(f'Media final: {round(nova_media, 1)}')