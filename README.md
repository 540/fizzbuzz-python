# Kata FizzBuzz

## Enunciado

Escribe un programa que imprima los números del 1 al 100, pero aplicando las siguientes normas:
- Devuelve Fizz si el número es divisible por 3.
- Devuelve Buzz si el número es divisible por 5.
- Devuelve FizzBuzz si el número es divisible por 3 y por 5.

Salida de ejemplo:

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
... etc hasta el 100
```

### Nuevos requerimientos

- Un número es Fizz si es divisible por 3 o si incluye un 3 en el número
- Un número es Buzz si es divisible por 5 o si incluye un 5 en el número

## Soluciones

En ramas se pueden ver diferentes soluciones de la kata

- **basic reqs** Solución de requisitos básicos usando una aproximación intermedia mediante función que devuelve la solución para cada número.
- **predicates-rules-openclose** Solución con requisitos nuevos Open-close con predicados y reglas mediante función que devuelve la solución para cada número.
- **one-to-many-1..4** Solución basada en _predicates-rules-openclose_ que hace el paso de ir de la solución de cada número al listado. Paso a paso en 4 iteraciones siempre en verde.

## Créditos

[Kata original](https://codingdojo.org/kata/FizzBuzz/)
