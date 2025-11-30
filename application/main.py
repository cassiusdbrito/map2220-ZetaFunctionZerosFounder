from application.ZetaFunction import ZetaFunction
from application.SecantMethod import SecantMethod
from graphics.graphics import plot_zeros  


def testar_intervalos(intervalos, max_iter=50, tol=1e-8):
    zf = ZetaFunction()
    sec = SecantMethod()

    zeros = []
    iteracoes = []
    intervalos_ok = []  

    print(f"============ TESTE : PARA {max_iter} ITERAÇÕES POR INTERVALO =============:")

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
    (13.63, 14.63),
    (20.52, 21.52),
    (24.51, 25.51),
    (29.92, 30.92),
    (32.43, 33.43),
    (37.08, 38.08),
    (40.41, 41.41),
    (42.83, 43.83),
    (47.50, 48.50),
    (49.27, 50.27),
    (52.47, 53.47),
    (55.95, 56.95),
    (58.85, 59.85),
    (60.33, 61.33),
    (64.61, 65.61),
    (66.58, 67.58),
    (68.55, 70.55),
    (71.07, 73.07),
    (74.70, 76.70),
    (76.14, 78.14),
    (78.34, 80.34),
    (81.91, 83.91),
    (83.74, 85.74),
    (86.43, 88.43),
    (87.81, 89.81),
    (91.49, 93.49),
    (93.65, 95.65),
    (94.87, 96.87),
    (97.83, 99.83),
    (100.32, 102.32),
    (102.73, 104.73),
    (104.45, 106.45),
    (106.17, 108.17),
    (110.03, 112.03),
    (110.87, 112.87),
    (113.32, 115.32),
    (115.23, 117.23),
    (117.79, 119.79),
    (120.37, 122.37),
    (121.95, 123.95),
    (123.26, 125.26)
    ]

    testar_intervalos(intervalos, max_iter=1000, tol=1e-10)

