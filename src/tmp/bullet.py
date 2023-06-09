""" import pygame as pg
from config import Config
from utils.asset_loader import AssetLoader


# TODO: tidy this up
# 3 entites can spawn bullets: Assist, Player, and Enemy
# 
class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y, is_enemy=False):
        super().__init__()
        if is_enemy:
            self.image = AssetLoader.load_enemy_bullet()
            self.speed = -Config.BULLET_SPEED*0.75
        else:
            self.image = AssetLoader.load_player_bullet()
            self.mask = pg.mask.from_surface(self.image)
            self.speed = Config.BULLET_SPEED
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery =y
        self._is_enemy = is_enemy #use this later to check whether bullet is damaging?
        
    def update(self, sprite_handler, dt):
        self.rect.move_ip(self.speed*dt, 0)
        if self.rect.centerx >= Config.WIDTH or self.rect.centerx <= 0:
            self.kill()
            
    def draw(self, screen):
        # can add other things to draw here
        screen.blit(self.image, self.rect) """