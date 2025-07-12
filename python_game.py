# JUEGO INTERACTIVO DE PYTHON - APRENDE PROGRAMANDO

def mostrar_bienvenida():
    print("""
    🐍 BIENVENIDO A PYTHON ADVENTURE 🐍
    Responde 30 preguntas y conviértete en experto en Python!
    """)

def jugar():
    puntaje = 0
    nombre = input("👋 ¿Cuál es tu nombre? >> ")
    
    print(f"\nHola {nombre}! Responde correctamente para sumar puntos:\n")

    # Lista de preguntas y respuestas
    preguntas = [
        {
            "pregunta": "1. ¿Cómo se imprime 'Hola mundo' en Python?",
            "opciones": ["a) print('Hola mundo')", "b) echo('Hola mundo')", "c) console.log('Hola mundo')"],
            "respuesta": "a"
        },
        {
            "pregunta": "2. ¿Qué tipo de dato se usa para texto en Python?",
            "opciones": ["a) str", "b) txt", "c) string"],
            "respuesta": "a"
        },
        {
            "pregunta": "3. ¿Cómo se define una función en Python?",
            "opciones": ["a) def mi_funcion():", "b) function mi_funcion():", "c) func mi_funcion():"],
            "respuesta": "a"
        },
        {
            "pregunta": "4. ¿Qué hace `len(lista)` en Python?",
            "opciones": ["a) Cuenta los elementos de una lista", "b) Ordena la lista", "c) Elimina el último elemento"],
            "respuesta": "a"
        },
        {
            "pregunta": "5. ¿Cuál es el resultado de `3 + 2 * 4`?",
            "opciones": ["a) 20", "b) 11", "c) 14"],
            "respuesta": "b"
        },
        {
            "pregunta": "6. ¿Cómo se comenta una línea en Python?",
            "opciones": ["a) // Comentario", "b) # Comentario", "c) /* Comentario */"],
            "respuesta": "b"
        },
        {
            "pregunta": "7. ¿Qué método se usa para añadir un elemento al final de una lista?",
            "opciones": ["a) lista.add()", "b) lista.append()", "c) lista.insert()"],
            "respuesta": "b"
        },
        {
            "pregunta": "8. ¿Qué hace `range(5)` en Python?",
            "opciones": ["a) Crea una lista [0, 1, 2, 3, 4]", "b) Crea una lista [1, 2, 3, 4, 5]", "c) Genera números aleatorios"],
            "respuesta": "a"
        },
        {
            "pregunta": "9. ¿Qué imprime `print(type(5.5))`?",
            "opciones": ["a) <class 'int'>", "b) <class 'float'>", "c) <class 'decimal'>"],
            "respuesta": "b"
        },
        {
            "pregunta": "10. ¿Cómo se convierte un número a texto?",
            "opciones": ["a) str(5)", "b) int('5')", "c) float(5)"],
            "respuesta": "a"
        },
        {
            "pregunta": "11. ¿Qué operador se usa para potencia?",
            "opciones": ["a) ^", "b) **", "c) *"],
            "respuesta": "b"
        },
        {
            "pregunta": "12. ¿Qué hace `'hola'.upper()`?",
            "opciones": ["a) Convierte a minúsculas", "b) Convierte a mayúsculas", "c) Cuenta las letras"],
            "respuesta": "b"
        },
        {
            "pregunta": "13. ¿Qué estructura se usa para pares clave-valor?",
            "opciones": ["a) Lista", "b) Tupla", "c) Diccionario"],
            "respuesta": "c"
        },
        {
            "pregunta": "14. ¿Qué bucle se ejecuta mientras una condición sea verdadera?",
            "opciones": ["a) for", "b) while", "c) loop"],
            "respuesta": "b"
        },
        {
            "pregunta": "15. ¿Qué imprime `print('Python'[1:3])`?",
            "opciones": ["a) 'Pyt'", "b) 'yth'", "c) 'tho'"],
            "respuesta": "b"
        },
        {
            "pregunta": "16. ¿Qué significa `==` en Python?",
            "opciones": ["a) Asignación", "b) Comparación de igualdad", "c) Diferente"],
            "respuesta": "b"
        },
        {
            "pregunta": "17. ¿Cómo se importa un módulo?",
            "opciones": ["a) include math", "b) import math", "c) require math"],
            "respuesta": "b"
        },
        {
            "pregunta": "18. ¿Qué método divide un string en una lista?",
            "opciones": ["a) split()", "b) join()", "c) replace()"],
            "respuesta": "a"
        },
        {
            "pregunta": "19. ¿Qué estructura es inmutable?",
            "opciones": ["a) Lista", "b) Tupla", "c) Diccionario"],
            "respuesta": "b"
        },
        {
            "pregunta": "20. ¿Qué imprime `print(10 / 3)`?",
            "opciones": ["a) 3", "b) 3.333...", "c) 3.0"],
            "respuesta": "b"
        },
        {
            "pregunta": "21. ¿Qué función detiene el programa por X segundos?",
            "opciones": ["a) time.sleep()", "b) wait()", "c) delay()"],
            "respuesta": "a"
        },
        {
            "pregunta": "22. ¿Qué módulo genera números aleatorios?",
            "opciones": ["a) random", "b) math", "c) numpy"],
            "respuesta": "a"
        },
        {
            "pregunta": "23. ¿Qué hace `' Hola '.strip()`?",
            "opciones": ["a) Elimina espacios al inicio y final", "b) Convierte a mayúsculas", "c) Divide el string"],
            "respuesta": "a"
        },
        {
            "pregunta": "24. ¿Qué operador verifica si un elemento está en una lista?",
            "opciones": ["a) ==", "b) in", "c) contains"],
            "respuesta": "b"
        },
        {
            "pregunta": "25. ¿Qué método une elementos de una lista en un string?",
            "opciones": ["a) concat()", "b) join()", "c) merge()"],
            "respuesta": "b"
        },
        {
            "pregunta": "26. ¿Qué estructura NO permite duplicados?",
            "opciones": ["a) Lista", "b) Conjunto (set)", "c) Tupla"],
            "respuesta": "b"
        },
        {
            "pregunta": "27. ¿Qué imprime `print(3 * 'a')`?",
            "opciones": ["a) 'aaa'", "b) '3a'", "c) Error"],
            "respuesta": "a"
        },
        {
            "pregunta": "28. ¿Qué módulo permite trabajar con archivos?",
            "opciones": ["a) os", "b) sys", "c) file"],
            "respuesta": "a"
        },
        {
            "pregunta": "29. ¿Qué hace `lista[::-1]`?",
            "opciones": ["a) Ordena la lista", "b) Invierte la lista", "c) Elimina el último elemento"],
            "respuesta": "b"
        },
        {
            "pregunta": "30. ¿Qué significa `try` y `except` en Python?",
            "opciones": ["a) Definir funciones", "b) Manejar errores", "c) Crear bucles"],
            "respuesta": "b"
        }
    ]

    # Mostrar preguntas y verificar respuestas
    for pregunta in preguntas:
        print(pregunta["pregunta"])
        for opcion in pregunta["opciones"]:
            print(opcion)
        
        respuesta_usuario = input("Tu respuesta (a/b/c): ").lower()
        
        if respuesta_usuario == pregunta["respuesta"]:
            print("✅ ¡Correcto! +10 puntos\n")
            puntaje += 10
        else:
            print(f"❌ Incorrecto. La respuesta era: {pregunta['respuesta']}\n")

    # Resultado final
    print(f"\n=== RESULTADO FINAL ===")
    print(f"{nombre}, obtuviste {puntaje}/300 puntos")
    
    if puntaje >= 250:
        print("🏆 ¡Eres un experto en Python!")
    elif puntaje >= 150:
        print("👍 ¡Buen trabajo! Sigue practicando")
    else:
        print("💡 Sigue aprendiendo, ¡Python es divertido!")

# Iniciar el juego
mostrar_bienvenida()
jugar()