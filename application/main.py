from ZetaFunction import ZetaFunction
from SecantMethod import SecantMethod


def testar_intervalos(intervalos, max_iter=50, tol=1e-8):
    zf = ZetaFunction()
    sec = SecantMethod()

    zeros = []
    iteracoes = []

    print(f"============ TESTE : PARA {max_iter} ITERAÇÕES =============:")

    for (p0, p1) in intervalos:
        try:
            raiz, it = sec.solve(zf, p0, p1, TOL=tol, N=max_iter)
            zeros.append(raiz)
            iteracoes.append(it)
        except Exception as e:
            print(f"Falha no intervalo [{p0}, {p1}]: {e}")

    print(f"\nquantidade de zeros encontrados: {len(zeros)}\n")

    for i, (t, it) in enumerate(zip(zeros, iteracoes), start=1):
        print(f"zero ({i}): t = {t:.12f}  |  interação = {it}")


if __name__ == "__main__":
    # Intervalos aproximados dos primeiros zeros reais
    intervalos = [
        (13.0, 15.0),
        (17.0, 18.5),
        (20.0, 23.0),
        (25.0, 27.0),
        (30.0, 33.0),
    ]

    testar_intervalos(intervalos, max_iter=50, tol=1e-7)
