class MotorFisico:

    def __init__(self, mud_weight, profundidad):

        self.mud_weight = mud_weight
        self.profundidad = profundidad

    def presion_hidrostatica(self):

        # P = 0.052 × MW × TVD
        presion = 0.052 * self.mud_weight * self.profundidad
        return presion

    def ecd(self, perdida_anular):

        ecd = self.mud_weight + (perdida_anular / (0.052 * self.profundidad))
        return ecd

    def detectar_kick(self, presion_formacion):

        presion_h = self.presion_hidrostatica()

        if presion_formacion > presion_h:
            return True
        else:
            return False
