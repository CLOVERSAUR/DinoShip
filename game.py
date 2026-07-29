#Incomplete stuff

class Game:

    def __init__(self):

        self.world = World()

        self.screen = Screen()
        
        self.screen.panels.append(
            MapPanel(self.world)
        )

        self.running = True

    def run(self):

        while self.running:

            self.screen.draw()

            command = self.screen.input()

            if command == "quit":
                self.running = False

            self.world.update(command)
