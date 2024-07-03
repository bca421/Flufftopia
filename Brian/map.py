import pygame
import pytmx

class TiledMap:
    def __init__(self, filename):
        # Load the TMX file using pytmx
        self.tmxdata = pytmx.load_pygame(filename, pixelalpha=True)
        # Calculate the map width and height in pixels
        self.width = self.tmxdata.width * self.tmxdata.tilewidth
        self.height = self.tmxdata.height * self.tmxdata.tileheight

    def render(self, surface):
        # Get tile image by global ID
        ti = self.tmxdata.get_tile_image_by_gid
        # Loop through visible layers in the TMX data
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                # Loop through each tile in the layer
                for x, y, gid in layer:
                    tile = ti(gid)
                    if tile:
                        # Draw the tile on the given surface
                        surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))

    def make_map(self):
        # Create a surface to render the map onto
        temp_surface = pygame.Surface((self.width, self.height))
        # Render the map onto the surface
        self.render(temp_surface)
        return temp_surface

class MapManager:
    def __init__(self):
        # Initialize with no current map
        self.current_map = None

    def load_map(self, filename):
        # Load the map from the given filename
        self.current_map = TiledMap(filename)

    def render_map(self, surface):
        if self.current_map:
            # Render the current map onto the given surface
            surface.blit(self.current_map.make_map(), (0, 0))
