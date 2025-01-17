import pygame
import sys

# Inicialización de pygame
pygame.init()

# Dimensiones de la ventana
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Menú de Juego")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fuente
font = pygame.font.SysFont("Arial", 30)
small_font = pygame.font.SysFont("Arial", 20)

# Cargar imagen
image = pygame.image.load('src/img/flecha_izq.png')  # Reemplaza con la ruta a tu imagen
image = pygame.transform.scale(image, (50, 50))  # Escalar la imagen si es necesario

# Funciones del menú
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)
    return textrect  # Retorna el rectángulo del texto para detectar clics

def menu():
    while True:
        screen.fill(WHITE)

        # Títulos
        play_button = draw_text("Jugar", font, BLACK, screen, width // 2, height // 2 - 40)
        scores_button = draw_text("Ver Máximas Puntuaciones", font, BLACK, screen, width // 2, height // 2)
        credits_button = draw_text("Créditos", font, BLACK, screen, width // 2, height // 2 + 40)

        # Detectar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                # Detectar clic en los botones
                if play_button.collidepoint(mouse_x, mouse_y):
                    play_game()
                elif scores_button.collidepoint(mouse_x, mouse_y):
                    show_scores()
                elif credits_button.collidepoint(mouse_x, mouse_y):
                    show_credits()

        pygame.display.update()

def play_game():
    print("Iniciar el juego...")
    # Aquí iría la lógica para iniciar el juego
    menu()  # Volver al menú después de jugar

def show_scores():
    print("Mostrar máximas puntuaciones...")
    # Aquí iría la lógica para mostrar las puntuaciones
    menu()  # Volver al menú después de ver las puntuaciones

def show_credits():
    while True:
        screen.fill(WHITE)

        # Títulos de los créditos
        draw_text("Créditos del Juego", font, BLACK, screen, width // 2, height // 6)
        draw_text("Nombre del Juego: Super Juego", small_font, BLACK, screen, width // 2, height // 3)
        draw_text("Versión: 1.0", small_font, BLACK, screen, width // 2, height // 3 + 40)
        draw_text("Programador: Tu Nombre", small_font, BLACK, screen, width // 2, height // 3 + 80)
        draw_text("Diseñador: Nombre del Diseñador", small_font, BLACK, screen, width // 2, height // 3 + 120)
        draw_text("Copyright 2025 - Todos los derechos reservados", small_font, BLACK, screen, width // 2, height // 3 + 160)
        screen.blit(image, (width-75, height-75))

        # Dibujar flecha hacia abajo


        # Detectar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Volver al menú cuando se haga clic
                menu()

        pygame.display.update()

# Ejecutar el menú
menu()
