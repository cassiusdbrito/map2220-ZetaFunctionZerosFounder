import math
import cmath

class GammaFunction:
    """
    Implementação da função Gamma complexa usando a 
    fórmula de Lanczos (g=7, n=9).

    Pode ser usada para qualquer número complexo z.
    """

    def __init__(self):
        # Coeficientes clássicos do método de Lanczos
        self.p = [
            0.99999999999980993,
            676.5203681218851,
            -1259.1392167224028,
            771.32342877765313,
            -176.61502916214059,
            12.507343278686905,
            -0.13857109526572012,
            9.9843695780195716e-6,
            1.5056327351493116e-7
        ]
        self.g = 7

    def gamma(self, z: complex) -> complex:
        """
        Implementação da fórmula de Lanczos.
        """

        # Reflexão se Re(z) < 0.5
        if z.real < 0.5:
            return math.pi / (cmath.sin(math.pi * z) * self.gamma(1 - z))

        z -= 1
        x = self.p[0]
        for i in range(1, len(self.p)):
            x += self.p[i] / (z + i)

        t = z + self.g + 0.5
        return math.sqrt(2 * math.pi) * t**(z + 0.5) * cmath.exp(-t) * x

    def __call__(self, z: complex) -> complex:
        return self.gamma(z)
