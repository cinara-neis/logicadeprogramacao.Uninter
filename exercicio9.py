a = int(input('Digite o primeiro lado do triangulo: '))
b = int(input('Digite o segundo lado do triangulo: '))
c = int(input('Digite o terceiro lado do triangulo: '))

if(a > 0) and (b > 0) and (c > 0):
    if(a + b > c) and (a + c > b) and (b + c > a):
        if a != b and a != c and b != c:
            print('triangulo escaleno')
        else:
            if a == b and a == c and b == c:
                print('Triangulo equilatero')
            else:
                print('triangulo isósceles')
    else:
        print('Ao menos um dos valores indicados não servem para formar um triangulo')
else:
    print('Ao menos um dos valores indicados não servem para formar um triangulo')
