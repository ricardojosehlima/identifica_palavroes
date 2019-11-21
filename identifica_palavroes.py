import re

# 1-) Presença de palavrões

texto = input("Digite uma frase: ")
listexto = texto.split(' ')

palavrao = re.compile(r'((?i)\bm[e3]rd\S+\b)|(?i)\bb[o0]st\S+\b|(?i)\bput[^r]\S*\b|(?i)\bp[o0]rr[a@4]\S*\b|(?i)\bc[uú](\b|z\w+)|(?i)\bv[i1](nh)?[a@4]d[^u]\S*\b|(?i)\b[kc][o0a@4]?r[o0a@4]?l[hi]?[o0a@4]?\S*\b|(?i)\bf[o0u]d\S+\b|\b[fF](\.)?[dD](\.)?[pP]\b|\b[Pp](\.)?[Qq](\.)?[pP]\b|\b[Vv][Ss][Ff]\b|\b[Vv][Tt][Nn][Cc]\b|(?i)b[o0u]c[e3]t\S+\b|(?i)\bpunh[e3]t\S+\b|(?i)\bb[i1](ch|x)[a@4]s?\b|\b(?i)c[o0]c[0ô]s?\b|\b(?i)[e3]scr[o0]t\S+\b|(?i)\bb[a@4]b[a@4][qc]\S+\b|(?i)\bc[a@4]g\S+\b|(?i)\bs[a@4]c[a@4]n[a@4e31i]\S*\b|(?i)\bk[a@4]c[e3]?t[e3]?\S*\b')
numero = re.compile(r'\b\S*\d+\S*\b')
caracteres_estranhos = re.compile(r'(?i)\b\S*[*.,!\^/@#$%&?]\S*\b')

lista_palavrao = list(filter(palavrao.match, listexto))
lista_numero = list(filter(numero.match, listexto))
lista_caracteres_estranhos = list(filter(caracteres_estranhos.match, listexto))


if len(lista_palavrao) == 1:
    print("Você escreveu o seguinte palavrão: ", lista_palavrao)
    print("""
    Você escreveu um palavrão. O registro escrito adotado pelo Enem proíbe esse tipo de termo e a gente concorda com isso.
    Afinal, você está sendo convidado a argumentar e usar palavrão não ajuda em nada sua argumentação.
    Sua redação vai receber nota zero e não vai ser corrigida.
    """)
elif len(lista_palavrao) > 1:
    print("Você escreveu os seguintes palavrões: ", lista_palavrao)
    print("""
    Você escreveu vários palavrões. Pense porque você fez isso. Lembre-se que você tem que argumentar.
    Usar palavrões não vai melhorar sua argumentação. O registro escrito adotado pelo Enem proíbe esse tipo de termo.
    Sua redação vai receber nota zero e não vai ser corrigida.
    """)
else:
    print("""
    Seu texto não possui palavrões.
    """)

if len(lista_numero) >= 1:
    print("Você usou a(s) seguinte(s) palavra(s) com números no meio: ", lista_numero)
    print("""
    Reveja o texto que você escreveu, pois o mesmo contém palavras com números no meio, o que não é aceito no
    registro adotado pelo Enem.
    """)

if len(lista_caracteres_estranhos) >= 1:
    print("Você usou a(s) seguinte(s) palavra(s) com caracteres estranhos no meio: ", lista_caracteres_estranhos)
    print("""
    Reveja o texto que você escreveu, pois o mesmo contém palavras com caracteres estranhos no meio, o que não é aceito no
    registro adotado pelo Enem.
    """)
