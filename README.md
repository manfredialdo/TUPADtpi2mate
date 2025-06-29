# tupad matematica1: Recuperatorio trabajo practico integrador nro2, 2025, manfredi, pighin

---

## 📹 Video Explicativo

[https://www.youtube.com/watch?v=Sxsgc6xGZ-Q](https://www.youtube.com/watch?v=Sxsgc6xGZ-Q)

---

## 📄 Recuperatorio del Trabajo Práctico Integrador 2 de Matemáticas

* **Archivo del recuperatorio:** `mate1tpi2recu.pdf`
* **Código de scripts juntos:** `tpi2recumate.py`

---

### 📝 `scriptparte1a.py`

Este script se enfoca en la lógica principal y evaluación de condiciones basadas en los DNIs.

* **`función dni_a_conjunto`**: Toma los DNIs y devuelve el conjunto de los elementos de un DNI.
* **`función condicion1`**: Toma dos conjuntos y devuelve `True` si la suma de los elementos de la diferencia es impar.
* **`función condicion2`**: A partir de dos conjuntos, devuelve `True` si la intersección tiene al menos 5 elementos.
* **`función inicio`**: Es la encargada de verificar la lógica e imprimir el resultado.

**💡 IDEA LÓGICA:** Si se cumplen ambas condiciones (condicion1 y condicion2), mostrar en pantalla “**a estudiar**”; de lo contrario, “**ver pelis**”.

---

### 📝 `scriptparte1b.py`

Este script verifica el resultado de condiciones adicionales, siguiendo el ejemplo de la consigna.

* **`condicion3`**: Si todos los conjuntos tienen al menos 5 elementos, entonces se considera que hay una **alta diversidad numérica**.
* **`condicion4`**: Si algún dígito aparece en todos los conjuntos, se marca como **dígito común**.
* **`condicion5`**: Si la intersección entre todos los conjuntos tiene exactamente un elemento, se considera un **dígito representativo del grupo**.

**Funciones implementadas:**

* **`dni_a_conjunto`**: Toma un DNI y devuelve un conjunto (función reutilizada).

**CÁLCULOS:**

* **`condicion3(a, b)`**: Toma dos DNIs y nos devuelve si hay alta diversidad numérica.
* **`condicion4(a,b)`**: Toma los dos DNIs y devuelve `True` si la intersección tiene más de un elemento.
* **`condicion5(a,b)`**: Toma dos DNIs y devuelve `True` si la intersección tiene exactamente un elemento.

**LÓGICA `inicio`**: Es la encargada de tomar los DNIs e imprimir los resultados.

---

### 📝 `scriptparte2a.py`

*(Para el código, ver anexo)*

Este script permite operaciones con DNIs, incluyendo ingreso manual y generación aleatoria, y realiza diversos cálculos y visualizaciones, además de evaluar condiciones.

**Operaciones con DNIs:**

* Ingreso de los DNIs (reales o ficticios).
* Opción de generación automática de los conjuntos de dígitos únicos.

El script `scriptparte2a.py` ofrece la opción de ingreso manual de DNIs y la generación aleatoria de DNIs. Luego realiza todos los siguientes cálculos y su posterior visualización, y además evalúa si se cumplen algunas condiciones y muestra el resultado.

**CÁLCULO Y VISUALIZACIÓN DE:**

* Unión, intersección, diferencias y diferencia simétrica.
* La frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas.
* Suma total de los dígitos de cada DNI.

**CONDICIONES:** Tomando los ejemplos de la consigna sobre evaluación de condiciones, vinculadas con las expresiones escritas…

* Si un dígito aparece en todos los conjuntos, mostrar "**Dígito compartido**".
* Si algún conjunto tiene más de 6 elementos, mostrar "**Diversidad numérica alta**".

Se implementa una función para cada tarea, realizando la operación y visualización de cada cálculo, además de las condiciones lógicas.

---

### 📝 `scriptparte2b.py`

*(Para el código, ver anexo)*

Este script se centra en operaciones y análisis relacionados con los años de nacimiento.

**Operaciones con años de nacimiento:**

* Ingreso de los años de nacimiento.
* Implementar una función para determinar si un año es **bisiesto**.
* Si alguno nació en año bisiesto, mostrar "**Tenemos un año especial**".
* Calcular el **producto cartesiano** entre el conjunto de años y el conjunto de edades actuales.
* Si todos nacieron después del 2000, mostrar "**Grupo Z**".
* Si dos o más integrantes del grupo tienen el mismo año, mostrar “**los dos nacieron el mismo año**”.
* Contar cuántos nacieron en **años pares e impares** utilizando estructuras repetitivas.

Se implementa una función para cada tarea, realizando la operación y visualización de cada cálculo, y se evalúan y muestran los resultados de las condiciones lógicas.
