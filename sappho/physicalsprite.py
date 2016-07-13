import pygame


class PhysicalSprite(pygame.sprite.Sprite):
    """A sprite with a position and collision data.

    Especially useful for sprites whose state changes
    a lot, notably through its update_state() method,
    affecting its mask, rect.

    Attributes:
        sprite (pygame.Sprite): The sprite which represents
            this actor, and from which the actor's mask and
            rect are derived every call to update_state().
        rect (pygame.Rect): Rectangle whose dimensions
            are updated (update_state) to reflect that
            of the sprite's rect dimensions. Absolute position
            of the Actor is set by setting this rect's:
            topleft, center, etc.
        mask (pygame.Mask): Reference to sprite's mask,
            which is updated every update_state().

    """

    def __init__(self, sprite):
        """Create a PhysicalSprite, using data from the
        supplied sprite.

        Arguments:
            sprite (pygame.Sprite): A Pygame sprite with the
                special attribute of mask and special method
                of update_state(). QUACK!

        """

        super(PhysicalSprite, self).__init__()

        self.sprite = sprite
        self.rect = self.sprite.rect
        self.mask = self.sprite.mask

    def update_state(self, timedelta):
        """Set the rect and mask attributes after updating
        the sprite's state.

        Arguments:
            timedelta (int): Typically the clock timedelta
                resulting from the game's clock.get_time().

        """

        self.sprite.update_state(timedelta)
        self.rect.size = self.sprite.size
        self.mask = self.sprite.mask
