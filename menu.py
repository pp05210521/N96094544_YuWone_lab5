import pygame
import os

# load images
MENU_IMAGE = pygame.image.load(os.path.join("images", "upgrade_menu.png"))
UPGRADE_IMAGE = pygame.image.load(os.path.join("images", "upgrade.png"))
SELL_IMAGE = pygame.image.load(os.path.join("images", "sell.png"))

# size of images
MENU_IMAGE_SIZES = (190, 190)
UPGRADE_IMAGE_SIZES = (50, 35)
SELL_IMAGE_SIZES = (35, 35)

# change sizes
menu_images = pygame.transform.scale(MENU_IMAGE, MENU_IMAGE_SIZES)
upgrade_images = pygame.transform.scale(UPGRADE_IMAGE, UPGRADE_IMAGE_SIZES)
sell_images = pygame.transform.scale(SELL_IMAGE, SELL_IMAGE_SIZES)


class UpgradeMenu:
    def __init__(self, x, y):
        # center (x, y)
        self.x = x
        self.y = y
        # set Buttons
        self.__buttons = [Button(upgrade_images, "upgrade", self.x , self.y - 75),
                          Button(sell_images, "sell", self.x , self.y + 75)]       
        
    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(menu_images, (self.x - MENU_IMAGE_SIZES[0]/2, self.y - MENU_IMAGE_SIZES[1]/2))
        # draw button
        win.blit(upgrade_images, (self.x - UPGRADE_IMAGE_SIZES[0]/2, self.y - 85))
        win.blit(sell_images, (self.x - SELL_IMAGE_SIZES[0]/2, self.y + 53))
        

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons


class Button:
    def __init__(self, image, name, x, y):
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        return self.rect.collidepoint(x, y) 

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name






