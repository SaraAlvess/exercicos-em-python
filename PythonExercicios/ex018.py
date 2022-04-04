from math import radians, sin, cos, tan
an = float(input('Digite um ângulo: '))
sen = sin(radians(an))
print('O ângulo {} tem o seno {:.2f}'.format(an, sen))
cos = cos(radians(an))
print('O ângulo {} tem o cosseno {:.2f}'.format(an, cos))
tan = tan(radians(an))
print('O ângulo {} tem a tangente {:.2f}'.format(an, tan))

