import math
import cmath
from GammaFunction import GammaFunction


class ZetaFunction:
    """
    Implementação aproximada da função Z(t) usando 
    Riemann–Siegel e Gamma complexa via Lanczos.
    """

    def __init__(self):
        self.gamma = GammaFunction()

    def theta(self, t: float) -> float:
        """
        θ(t) = Im(log Γ(1/4 + i t/2)) - (t/2) log π
        """
        z = 0.25 + 0.5j * t
        log_gamma = cmath.log(self.gamma(z))
        return log_gamma.imag - (t / 2.0) * math.log(math.pi)

    def Z(self, t: float) -> float:
        """
        Z(t) ≈ 2 Σ_{n ≤ sqrt(t/2π)} n^{-1/2} cos(θ(t) - t ln n)
        """

        if t <= 0:
            raise ValueError("t must be positive for the Riemann–Siegel approximation.")

        theta_t = self.theta(t)
        N = int(math.sqrt(t / (2 * math.pi)))

        total = 0.0
        for n in range(1, N + 1):
            total += (1.0 / math.sqrt(n)) * math.cos(theta_t - t * math.log(n))

        return 2.0 * total

    def __call__(self, t: float) -> float:
        return self.Z(t)
