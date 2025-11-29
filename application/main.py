from application.ZetaFunction import ZetaFunction
from application.SecantMethod import SecantMethod
from graphics.graphics import plot_zeros  


def testar_intervalos(intervalos, max_iter=50, tol=1e-8):
    zf = ZetaFunction()
    sec = SecantMethod()

    zeros = []
    iteracoes = []
    intervalos_ok = []  

    print(f"============ TESTE : PARA {max_iter} ITERAÇÕES =============:")

    for (p0, p1) in intervalos:
        try:
            raiz, it = sec.solve(zf, p0, p1, TOL=tol, N=max_iter)
            zeros.append(raiz)
            iteracoes.append(it)
            intervalos_ok.append((p0, p1))
        except Exception as e:
            print(f"Falha no intervalo [{p0}, {p1}]: {e}")

    print(f"\nquantidade de zeros encontrados: {len(zeros)}\n")

    for i, (t, it, (p0, p1)) in enumerate(zip(zeros, iteracoes, intervalos_ok), start=1):
        print(f"zero ({i}): t = {t:.12f}  |  interação = {it}  |  intervalo usado = [{p0}, {p1}]")

    if zeros:
        plot_zeros(zeros, iteracoes)


if __name__ == "__main__":
    intervalos = [
        (13, 15),
        (17, 18.5),
        (20, 23),
        (25, 27),
        (30, 33),
        (35, 38),
        (40, 43),
        (45, 48),
        (50, 53),
        (55, 58),
        (60, 63),
        (65, 68),
        ]

    testar_intervalos(intervalos, max_iter=1000, tol=1e-10)

