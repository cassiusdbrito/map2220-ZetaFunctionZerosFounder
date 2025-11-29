class SecantMethod:
    def solve(self, f, p0, p1, TOL=1e-8, N=50):
        """
        f  : função alvo (chamada como f(x))
        p0 : primeira aproximação inicial
        p1 : segunda aproximação inicial
        TOL: tolerância
        N  : máximo de iterações

        Retorna (p, iterações) ou lança erro se falhar.
        """

        q0 = f(p0)
        q1 = f(p1)

        for i in range(1, N + 1):
            if (q1 - q0) == 0:
                raise ZeroDivisionError("Denominador zero no método da secante.")

            p = p1 - q1 * (p1 - p0) / (q1 - q0)

            if abs(p - p1) < TOL:
                return p, i

            p0, q0 = p1, q1
            p1 = p
            q1 = f(p1)

        raise RuntimeError("Método da secante falhou: número máximo de iterações excedido.")
