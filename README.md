
    <h1>Documentación del Proyecto</h1>

    <p><strong>VIDEO EXPLICATIVO:</strong> <a href="https://www.youtube.com/watch?v=Sxsgc6xGZ-Q">https://www.youtube.com/watch?v=Sxsgc6xGZ-Q</a></p>

    <h2>Recuperatorio del Trabajo Práctico Integrador 2 de Matemáticas</h2>
    <p><strong>Archivo:</strong> mate1tpi2recu.pdf</p>
    <p><strong>Código de scripts juntos:</strong> tpi2recumate.py</p>

    <hr>

    <h3>scriptparte1a.py</h3>
    <ul>
        <li><strong>función dni_a_conjunto:</strong> toma los dnis, y nos devuelve el conjunto de los elementos de un dni.</li>
        <li><strong>función condicion1:</strong> toma los dos conjuntos y devuelve True si la suma de los elementos de la diferencia es impar.</li>
        <li><strong>función condicion2:</strong> a partir de dos conjuntos y devuelve True si la intersección tiene al menos 5 elementos.</li>
        <li><strong>función inicio:</strong> es la encargada de verificar la lógica e imprimir resultado.</li>
    </ul>
    <p><strong>IDEA LÓGICA:</strong> Si se cumplen ambas condiciones mostrar en pantalla “a estudiar” sino “ver pelis”.</p>

    <hr>

    <h3>scriptparte1b.py</h3>
    <p>Necesitamos que verifiquen el resultado de estas condiciones.. parte del ejemplo consigna…</p>
    <ul>
        <li><strong>condicion3:</strong> Si todos los conjuntos tienen al menos 5 elementos, entonces se considera que hay una alta diversidad numérica.</li>
        <li><strong>condicion4:</strong> Si algún dígito aparece en todos los conjuntos, se marca como dígito común.</li>
        <li><strong>condicion5:</strong> Si la intersección entre todos los conjuntos tiene exactamente un elemento, se considera un dígito representativo del grupo.</li>
    </ul>
    <p><strong>Funciones implementadas:</strong></p>
    <ul>
        <li><strong>dni_a_conjunto:</strong> toma un dni y devuelve un conjunto.</li>
    </ul>
    <p><strong>CÁLCULOS:</strong></p>
    <ul>
        <li><strong>condicion3(a, b):</strong> toma dos dni y nos devuelve si hay alta diversidad numérica.</li>
        <li><strong>condicion4(a,b):</strong> toma los dos dni y devuelve True si la intersección tiene más de un elemento.</li>
        <li><strong>condicion5(a,b):</strong> toma dos dnis y devuelve True si la intersección tiene exactamente un elemento.</li>
    </ul>
    <p><strong>LÓGICA inicio:</strong> es la encargada de tomar los dnis e imprimir los resultados.</p>

    <hr>

    <h3>scriptparte2a.py</h3>
    <p><strong>Documentación scriptparte2a.py (para código ver anexo)</strong></p>
    <p>Operaciones con DNIs - Ingreso de los DNIs (reales o ficticios)…</p>
    <ul>
        <li>Opción de generación automática de los conjuntos de dígitos únicos.</li>
    </ul>
    <p>El script scriptparte2a.py da la opción del ingreso manual de dnis y la generación aleatoria de dnis… luego realiza todos los siguientes cálculos y su posterior visualización, y además evalúa si se cumplen algunas condiciones y muestra el resultado.</p>
    <p><strong>CÁLCULO Y VISUALIZACIÓN DE:</strong></p>
    <ul>
        <li>Unión, intersección, diferencias y diferencia simétrica.</li>
        <li>La frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas.</li>
        <li>Suma total de los dígitos de cada DNI.</li>
    </ul>
    <p><strong>CONDICIONES:</strong> Tomando los ejemplos de la consigna sobre evaluación de condiciones, vinculadas con las expresiones escritas…</p>
    <ul>
        <li>Si un dígito aparece en todos los conjuntos, mostrar "Dígito compartido".</li>
        <li>Si algún conjunto tiene más de 6 elementos, mostrar "Diversidad numérica alta".</li>
    </ul>
    <p>Una función para cada tarea… Se realiza la operación y visualización de cada cálculo, y demás condiciones lógicas.</p>

    <hr>

    <h3>scriptparte2b.py</h3>
    <p><strong>(para el código, ver anexo)</strong></p>
    <p>Operaciones con años de nacimiento ·</p>
    <ul>
        <li>Ingreso de los años de nacimiento.</li>
        <li>Implementar una función para determinar si un año es bisiesto.</li>
        <li>Si alguno nació en año bisiesto, mostrar "Tenemos un año especial".</li>
        <li>Calcular el producto cartesiano entre el conjunto de años y el conjunto de edades actuales.</li>
        <li>Si todos nacieron después del 2000, mostrar "Grupo Z".</li>
        <li>Si dos o más integrantes del grupo tienen el mismo año, mostrar “los dos nacieron el mismo año”.</li>
        <li>Contar cuántos nacieron en años pares e impares utilizando estructuras repetitivas.</li>
    </ul>
    <p>Una función para cada tarea… Se realiza la operación y visualización de cada cálculo, y se evalúan y muestra resultado de las condiciones lógicas.</p>
