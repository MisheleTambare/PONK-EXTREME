import pygame
import sys
import random
import os

# Inicializar Pygame
pygame.init()
pygame.mixer.init()

# Dimensiones de la pantalla
ANCHO, ALTO = 1200, 650
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pong Extreme de Dos Jugadores")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROSADO = (255, 0, 100)

# Cargar imagen de fondo juego
fondo_path = os.path.join("fondos", "fondo_juego.png")
fondo = pygame.image.load(fondo_path)
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

# Cargar imagen de fondo inicio
fondo1_path = os.path.join("fondos", "fondo_inicio.png")
fondo1 = pygame.image.load(fondo1_path)
fondo1 = pygame.transform.scale(fondo1, (ANCHO, ALTO))

# Cargar imagen de fondo instrucciones
fondo2_path = os.path.join("fondos", "fondo_instrucciones.png")
fondo2 = pygame.image.load(fondo2_path)
fondo2 = pygame.transform.scale(fondo2, (ANCHO, ALTO))

# Agregar Música
pygame.mixer.music.load(os.path.join("fondos", "audio.mpeg"))

# Tamaño de la raqueta y velocidad
RAQUETA_ANCHO, RAQUETA_ALTO = 20, 100
VELOCIDAD_RAQUETA = 15

# Tamaño de la pelota y velocidad
PELOTA_DIAMETRO = 30
PELOTA_DIAMETRO_B = 50
VELOCIDAD_PELOTA_INICIAL = 8
AUMENTO_VELOCIDAD_TIEMPO = 5
AUMENTO_VELOCIDAD_FACTOR = 1.5

# Inicializar posiciones y velocidades
raqueta1_y = ALTO // 2 - RAQUETA_ALTO // 2
raqueta2_y = ALTO // 2 - RAQUETA_ALTO // 2
pelotas = [{'x': ANCHO // 2, 'y': ALTO // 2, 'dx': random.choice([1, -1]) * VELOCIDAD_PELOTA_INICIAL,
            'dy': random.choice([1, -1]) * VELOCIDAD_PELOTA_INICIAL}]
puntaje_jugador1 = puntaje_jugador2 = 0
temporizador = 0
mostrar_mensaje = False
mostrar_bienvenida = True

# Fuentes
fuente_grande = pygame.font.Font(None, 100)
fuente_mediana = pygame.font.Font(None, 50)
fuente_pequena = pygame.font.Font(None, 30)

# Función para mover las pelotas
def mover_pelotas(pelotas_movimiento):
    for pelota in pelotas_movimiento:
        pelota['x'] += pelota['dx']
        pelota['y'] += pelota['dy']

        # Rebote en las paredes
        if pelota['x'] <= 0 or pelota['x'] >= ANCHO - PELOTA_DIAMETRO_B:
            pelota['dx'] = -pelota['dx']
        if pelota['y'] <= 0 or pelota['y'] >= ALTO - PELOTA_DIAMETRO_B:
            pelota['dy'] = -pelota['dy']

# Reloj para controlar la velocidad de actualización
reloj = pygame.time.Clock()

# Función para mostrar la pantalla inicial
def pantalla_inicio():
    pelotas_bienvenida = [{'x': random.randint(0, ANCHO - PELOTA_DIAMETRO_B), 'y': random.randint(0, ALTO - PELOTA_DIAMETRO_B),
                           'dx': random.choice([1, -1]) * VELOCIDAD_PELOTA_INICIAL,
                           'dy': random.choice([1, -1]) * VELOCIDAD_PELOTA_INICIAL} for _ in range(20)]

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                if 350 <= x <= 550 and 370 <= y <= 420:
                    pantalla_instrucciones()
                elif 650 <= x <= 850 and 370 <= y <= 420:
                    return

        # Mover las pelotas en la pantalla de bienvenida
        mover_pelotas(pelotas_bienvenida)

        PANTALLA.blit(fondo1, (0, 0))

        # Dibujar pelotas en la pantalla de bienvenida
        for pelota in pelotas_bienvenida:
            pygame.draw.ellipse(PANTALLA, ROSADO, (pelota['x'], pelota['y'], PELOTA_DIAMETRO_B, PELOTA_DIAMETRO_B))

        texto_bienvenida = fuente_grande.render("PONG", True, BLANCO)
        PANTALLA.blit(texto_bienvenida, (510, 200))

        texto_bienvenida = fuente_grande.render("ESTREME", True, BLANCO)
        PANTALLA.blit(texto_bienvenida, (440, 280))

        pygame.draw.rect(PANTALLA, BLANCO, (350, 370, 200, 50))
        texto_instrucciones = fuente_pequena.render("Instrucciones", True, NEGRO)
        PANTALLA.blit(texto_instrucciones, (380, 385))

        pygame.draw.rect(PANTALLA, BLANCO, (650, 370, 200, 50))
        texto_jugar = fuente_pequena.render("Jugar", True, NEGRO)
        PANTALLA.blit(texto_jugar, (721, 385))

        pygame.display.flip()
        reloj.tick(60)

# Función para mostrar la pantalla de instrucciones
def pantalla_instrucciones():
    pelotas_instrucciones = [{'x': random.randint(0, ANCHO - PELOTA_DIAMETRO_B), 'y': random.randint(0, ALTO - PELOTA_DIAMETRO_B),
                              'dx': random.choice([1, -1]) * VELOCIDAD_PELOTA_INICIAL,
                              'dy': random.choice([1, -1]) * VELOCIDAD_PELOTA_INICIAL} for _ in range(20)]

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                if 500 <= x <= 700 and 550 <= y <= 600:
                    return
                
        # Mover las pelotas en la pantalla de instrucciones
        mover_pelotas(pelotas_instrucciones)

        PANTALLA.blit(fondo2, (0, 0))

        # Dibujar pelotas en la pantalla de instrucciones
        for pelota in pelotas_instrucciones:
            pygame.draw.ellipse(PANTALLA, ROSADO, (pelota['x'], pelota['y'], PELOTA_DIAMETRO_B, PELOTA_DIAMETRO_B))

        # Dibujar descripción del juego
        descripcion_juego1 = ("Sumérgete en la emoción de Pong Extreme, la versión moderna del clásico juego de ping pong en tu computadora.")
        descripcion_juego2 = ("Controla tu propio rectángulo en la pantalla y compite contra un oponente en un emocionante duelo.")
        texto_descripcion1 = fuente_pequena.render(descripcion_juego1, True, BLANCO)
        PANTALLA.blit(texto_descripcion1, (35, 70))
        texto_descripcion2 = fuente_pequena.render(descripcion_juego2, True, BLANCO)
        PANTALLA.blit(texto_descripcion2, (100, 110))

        # Dibujar objetivo del juego
        objetivo_juego1 = ("OBJETIVO DEL JUEGO:")
        objetivo_juego2 = ("Llegar a 10 puntos antes que tu oponente.")
        objetivo_juego3 = ("Cada vez que logres que la bola pase a tu adversario, ¡anotarás un punto!")
        texto_objetivo1 = fuente_mediana.render(objetivo_juego1, True, BLANCO)
        PANTALLA.blit(texto_objetivo1, (410, 160))
        texto_objetivo2 = fuente_pequena.render(objetivo_juego2, True, BLANCO)
        PANTALLA.blit(texto_objetivo2, (400, 210))
        texto_objetivo3 = fuente_pequena.render(objetivo_juego3, True, BLANCO)
        PANTALLA.blit(texto_objetivo3, (250, 250))

        # Dibujar reglas del juego
        reglas_juego1 = ("REGLAS DEL JUEGO:")
        reglas_juego2 = ("- El juego es para 2 jugadores, con el Jugador 1 controlando su rectángulo con las teclas W y S, y el Jugador 2 ")
        reglas_juego3 = ("utilizando las flechas de arriba y abajo del teclado.")
        reglas_juego4 = ("- Gana el primer jugador que alcance los 10 puntos.")
        reglas_juego5 = ("- La velocidad de la pelota aumenta cada 5 segundos, intensificando la emoción del juego.")
        reglas_juego6 = ("- Si un jugador deja pasar la bola, la velocidad vuelve a ser la inicial")
        texto_reglas1 = fuente_mediana.render(reglas_juego1, True, BLANCO)
        PANTALLA.blit(texto_reglas1, (425, 280))
        texto_reglas2 = fuente_pequena.render(reglas_juego2, True, BLANCO)
        PANTALLA.blit(texto_reglas2, (35, 320))
        texto_reglas3 = fuente_pequena.render(reglas_juego3, True, BLANCO)
        PANTALLA.blit(texto_reglas3, (50, 360))
        texto_reglas4 = fuente_pequena.render(reglas_juego4, True, BLANCO)
        PANTALLA.blit(texto_reglas4, (35, 400))
        texto_reglas5 = fuente_pequena.render(reglas_juego5, True, BLANCO)
        PANTALLA.blit(texto_reglas5, (35, 440))
        texto_reglas6 = fuente_pequena.render(reglas_juego6, True, BLANCO)
        PANTALLA.blit(texto_reglas6, (35, 480))

        pygame.draw.rect(PANTALLA, BLANCO, (500, 550, 200, 50))
        texto_atras = fuente_pequena.render("Atrás", True, NEGRO)
        PANTALLA.blit(texto_atras, (570, 565))

        pygame.display.flip()
        reloj.tick(60)

# Función principal del juego
def juego():
    global raqueta1_y, raqueta2_y, pelotas, puntaje_jugador1, puntaje_jugador2, temporizador, mostrar_mensaje, mostrar_bienvenida

    pygame.mixer.music.play(-1)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()

        if mostrar_bienvenida:
            pantalla_inicio()
            mostrar_bienvenida = False

        if not mostrar_mensaje:
            # Movimiento de las raquetas
            teclas = pygame.key.get_pressed()
            if teclas[pygame.K_UP] and raqueta2_y > 0:
                raqueta2_y -= VELOCIDAD_RAQUETA
            if teclas[pygame.K_DOWN] and raqueta2_y < ALTO - RAQUETA_ALTO:
                raqueta2_y += VELOCIDAD_RAQUETA
            if teclas[pygame.K_w] and raqueta1_y > 0:
                raqueta1_y -= VELOCIDAD_RAQUETA
            if teclas[pygame.K_s] and raqueta1_y < ALTO - RAQUETA_ALTO:
                raqueta1_y += VELOCIDAD_RAQUETA

            # Movimiento de la pelota
            for pelota in pelotas:
                pelota['x'] += pelota['dx']
                pelota['y'] += pelota['dy']

                # Rebote en las paredes superior e inferior
                if pelota['y'] <= 0 or pelota['y'] >= ALTO - PELOTA_DIAMETRO:
                    pelota['dy'] = -pelota['dy']

                # Rebote en las raquetas
                if (
                    pelota['x'] <= RAQUETA_ANCHO
                    and raqueta1_y <= pelota['y'] <= raqueta1_y + RAQUETA_ALTO
                ) or (
                    pelota['x'] >= ANCHO - RAQUETA_ANCHO - PELOTA_DIAMETRO
                    and raqueta2_y <= pelota['y'] <= raqueta2_y + RAQUETA_ALTO
                ):
                    pelota['dx'] = -pelota['dx']

                # Puntuación y reinicio de la pelota
                if pelota['x'] <= 0:
                    puntaje_jugador2 += 1
                    reiniciar_pelotas()

                if pelota['x'] >= ANCHO - PELOTA_DIAMETRO:
                    puntaje_jugador1 += 1
                    reiniciar_pelotas()

                # Verificar si alguien ha ganado
                if puntaje_jugador1 == 10 or puntaje_jugador2 == 10:
                    mostrar_mensaje = True

            # Actualizar temporizador
            temporizador += 1

            # Aumentar velocidad gradualmente cada 15 segundos
            if temporizador % (AUMENTO_VELOCIDAD_TIEMPO * 60) == 0:
                aumentar_velocidad()

        # Mostrar en pantalla
        PANTALLA.blit(fondo, (0, 0)) 
        pygame.draw.rect(PANTALLA, BLANCO, (RAQUETA_ANCHO, raqueta1_y, RAQUETA_ANCHO, RAQUETA_ALTO))
        pygame.draw.rect(PANTALLA, BLANCO, (ANCHO - 2 * RAQUETA_ANCHO, raqueta2_y, RAQUETA_ANCHO, RAQUETA_ALTO))

        for pelota in pelotas:
            pygame.draw.ellipse(PANTALLA, ROSADO, (pelota['x'], pelota['y'], PELOTA_DIAMETRO, PELOTA_DIAMETRO))

        # Mostrar puntaje en pantalla
        fuente1 = pygame.font.Font(None, 120)
        fuente2 = pygame.font.Font(None, 35)
        fuente3 = pygame.font.Font(None, 100)
        mensaje1 = f"{puntaje_jugador1}    {puntaje_jugador2}"  
        mensaje2 = f"Tiempo: {temporizador // 60}"
        texto1 = fuente1.render(mensaje1, True, BLANCO)
        texto2 = fuente2.render(mensaje2, True, BLANCO)
        PANTALLA.blit(texto1, (ANCHO // 2.35 , 20))
        PANTALLA.blit(texto2, (ANCHO // 1.15 , 580))

        # Mostrar mensaje de ganador si hay un ganador
        if mostrar_mensaje:
            ganador = "Jugador 1" if puntaje_jugador1 == 10 else "Jugador 2"
            mensaje_ganador = f"¡{ganador} ganó!"
            texto_ganador = fuente3.render(mensaje_ganador, True, BLANCO)
            PANTALLA.blit(texto_ganador, (ANCHO // 4, ALTO // 2))

        pygame.display.flip()
        reloj.tick(60)

# Función para reiniciar la posición de las pelotas
def reiniciar_pelotas():
    global pelotas
    pelotas = [{'x': ANCHO // 2, 'y': ALTO // 2, 'dx': random.choice([1, -1]) * VELOCIDAD_PELOTA_INICIAL, 'dy': random.choice([1, -1]) * VELOCIDAD_PELOTA_INICIAL}]

# Función para aumentar la velocidad de la pelota gradualmente
def aumentar_velocidad():
    global pelotas
    for pelota in pelotas:
        pelota['dx'] *= AUMENTO_VELOCIDAD_FACTOR
        pelota['dy'] *= AUMENTO_VELOCIDAD_FACTOR

# Iniciar el juego
juego()
