from ..ecs import component


class TransformComponent(component.Component):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.vx = 0
        self.vy = 0
        self.vz = 0
