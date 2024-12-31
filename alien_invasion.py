import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from time import sleep


class AlienInvasion:
    """Clase general para gestionar los recursos y el comportamiento del juego"""

    def __init__(self):
        """Inicializa el juego y crea recursos"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_width()
        self.settings.screen_height = self.screen.get_height()
        pygame.display.set_caption("Alien Invasion")

        #Creamos una instancia de GameStats para gestionar las estadisticas
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # creamos el boton play
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Inicia el bucle principal del juego"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

            #Hace visible los cambios de pantalla
            pygame.display.flip()

    def _check_events(self):
    # Busca eventos de teclado y ratón
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()
        elif  event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_j:
            self._start_game()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _check_play_button(self, mouse_pos):
        """ Inicia un juego nuevo cuando el jugador hace click en play. """
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()


    def _start_game(self):
        # Restablecemos las estadisticas del juego
        self.stats.reset_stats()
        self.stats.game_active = True
        self.settings.initialize_dynamic_settings()

        # eliminamos balas y aliens
        self.aliens.empty()
        self.bullets.empty()

        # Hacemos nueva flota y centramos la nave
        self._create_fleet()
        self.ship.center_ship()

        # ocultamos cursor del ratón
        pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """Crea una bala nueva y la añade al grupo bullets"""
        if(len(self.bullets)) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):

        self.bullets.update()

        # Se eliminan las balas que salen de la pantalla
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_aliens_collision()


    def _check_bullet_aliens_collision(self):
        #buscamps los impactos de las balas en los aliens
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            #destruye las balas y crea una flota nueva
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()


    def _create_fleet(self):
        """Creamos un alien y después la flota"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (alien_width * 2)
        number_aliens_x = available_space_x // (alien_width * 2)

        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3* alien_height) - ship_height
        alien_height = alien.rect.height
        number_rows = available_space_y // (2 * alien_height)

        #Creamos la flota de aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.y = alien_height + 2 * alien_height * row_number
        alien.rect.y = alien.y

        self.aliens.add(alien)

    def _update_aliens(self):
        """Comprobamos si algún alien esta en un borde,
        después actualizamos la posición de todos los aliens"""
        self._check_fleet_edges()
        self.aliens.update()

        # Busca colisiones alien-nave
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # Busca si algun alien ha llegado al fondo de la pantalla
        self._check_aliens_bottom()


    def _check_fleet_edges(self):
        """Responde adecuadamente si algún alien ha llegado a un borde"""
        for alien in self.aliens.sprites():
            if alien._check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """Baja toda la flota y cambia su dirección"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _update_screen(self):
        # Redibuja la pantalla en cada paso por el bucle
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Dibujamos el boton play, si el juego está inactivo
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


    def _ship_hit(self):
        """Responde al impacto de un alien con la nave"""

        # disminuimos una vida
        if self.stats.ships_left >=1:
            self.stats.ships_left -= 1
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

        # borramos aliens y balas
        self.aliens.empty()
        self.bullets.empty()

        # creamos nueva flota y centramos la nave
        self._create_fleet()
        self.ship.center_ship()

        # una pausa para insultar al ordenador
        sleep(0.5)


    def _check_aliens_bottom(self):
        """Comprueba si algún alien ha llegado a la parte baja de la pantalla"""

        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # hacemos lo mismo que si hubiera impactado con la nave
                self._ship_hit()
                break





# Crear una instancia del juego y ejecutarlo
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()