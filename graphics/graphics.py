import matplotlib.pyplot as plt

def plot_zeros(t_values, iterations):
    """
    Plota os zeros encontrados (t_values) contra o número de iterações da secante.
    """

    plt.figure(figsize=(12, 7)) 


    plt.scatter(t_values, iterations, s=120)

    plt.plot(t_values, iterations, linestyle='--')

    plt.xlabel("Valor de t (zero encontrado)", fontsize=14)
    plt.ylabel("Número de iterações da secante", fontsize=14)
    plt.title("Zeros encontrados x Número de iterações", fontsize=16)

    plt.grid(True, linewidth=0.5)

    plt.tight_layout()

    if t_values:
        min_t, max_t = min(t_values), max(t_values)
        plt.xlim(min_t * 0.9, max_t * 1.1)

    if iterations:
        min_i, max_i = min(iterations), max(iterations)
        plt.ylim(min_i * 0.9, max_i * 1.3)

    plt.show()
