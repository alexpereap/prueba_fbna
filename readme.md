# Ejercicios
Hola, gracias por revisar esta prueba!
Ejecutar los ejercicios usando python 3

## Ejercicio 1:
- Tiempo invertido en la solución: 30 minutos.
El grueso del ejercicio es el calculo de la media, para ello se deben tener en cuenta dos factores: <br/>
- 1. Si el numero es impar, es exactamente el numero en medio de la lista, este índice se puede obtener con la siguiente formula:<br/>
Math.floor( largo_de_la_lista / 2 )
- 2. Si el número es par, la media consiste en la suma de los dos números de en medio de la lista dividida por dos.<br/>
Siempre obtendremos el índice de la derecha con en el valor entero del siguiente calculo: largo_de_lista / 2.<br/>
El índice de la izquierda sera entonces indice_derecho - 1, al sumar el valor de estos dos índices en la lista y dividir por dos, obtenemos la media.

### Ejecución:
```sh
$ python exercise1_median/median.py
```

## Ejercicio 2:
- Tiempo invertido en la solución: 3 horas
Para este ejercicio, la estrategia que aplique, es encontrar el camino de nodo a a nodo b, una vez encontrado dicho camino, se analiza que colores están repetidos en dicho camino<br/>.
Para lograrlo, cree una clase Nodo para representar los nodos de los arboles, y un algoritmo trasversal que encuentra el camino entre el nodo raíz y nodoA y nodo raíz y nodoB, para así después encontrar el camino entre nodoA y nodoB<br/>

### Ejecución:
```sh
$ python exercise2_tree/tree.py
```

# Preguntas teóricas:
## ¿Cuales serian las cualidades para un código limpio? 
- Se debe seguir una guía de estilo, según el lenguaje que se este manejando, por ejemplo, en el caso de Python existe el estándar pep8 el cual dicta reglas para la escritura del código, como convención de nombres de las funciones, variables, espacios entre funciones e identación. Todo esto es en aras de que la lectura del código sea sencilla y agradable.<br/>

- El código debe estar muy bien comentado, y con uso de variables y nombres de funciones dicientes, para facilitar su futura modificación.<br/>

- Debe estar refactorizado en lo posible, para evitar redundancia de funciones.<br/>

- La ejecución debe ser optima, en lo posible mantener el tiempo y complejidad del algoritmo en niveles de ejecución rápida.<br/>

- Debe contar con un set de pruebas unitarias, con distintos casos de uso, para asegurar el buen funcionamiento de todo el proyecto al cambiar cualquier porción del código, y así evitar que un cambio en una característica, afecte el funcionamiento de forma negativa en otras características.<br/>

## ¿Cuales serian los estándares según tú para un buen proyecto? 
- A nivel de planeación, se deben tener muy claro los requerimientos, asegurarse que son alcanzables en el tiempo estipulado en el proyecto. Que se cuenta con los recursos y herramientas necesarias para su desarrollo. <br/>

- A nivel de ejecución, el proyecto debe estar bien documentado, para que futuros desarrolladores puedan modificarlo sin problema. También debe contar con un set de pruebas fuerte para mitigar al máximo la ocurrencia de bugs y fallos. Definir procesos de integración continua sería ideal, para así agilizar el desarrollo y la solución de fallas. <br/>

## ¿Qué patrones conoce? y utiliza?
- Separation of Concerns. <br/>
- MVC (model view controller). <br />
- Single responsability principle. <br/>
- Facade. <br/>
- DRY (don't repeat yourself). <br />