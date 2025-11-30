# Projeto: Busca de Zeros da Função Zeta de Riemann na Linha Crítica
**Disciplina:** MAP2220 – Métodos Numéricos  
**Objetivo:** Implementar, usando apenas as bibliotecas permitidas, uma ferramenta para aproximar zeros da função zeta de Riemann na linha crítica  
s = 1/2 + it,  
utilizando o **Método da Secante** conforme o algoritmo do livro **Burden, Faires & Burden – Fundamentos de Análise Numérica**.

---

## Descrição do Projeto

Este projeto implementa:

1. **Aproximação da função Zeta crítica** via fórmula truncada de Riemann–Siegel.  
2. **O método da Secante** para encontrar valores de t tais que Z(t) = 0.  
3. **Uma rotina de testes** para procurar zeros em intervalos crescentes.

---

## Metodologia

### 1. Aproximação da Função Zeta

A função implementada é:

Z(t) = 2 \sum_{n=1}^{N} n^{-1/2} cos( θ(t) − t ln n )

onde  
N = floor( sqrt( t / (2π) ) ).

A fase é dada por:

θ(t) = Im( log( Γ(1/4 + i t/2) ) ) − (t/2) log π.

Como o Python não possui `cmath.gamma`, foi criada uma classe própria **GammaFunction** utilizando a **aproximação de Lanczos**, totalmente dentro das restrições do professor.

---

### 2. Método da Secante

Implementado exatamente como no **Capítulo 2** do livro do **Burden**.  
Possui:

- Duas aproximações iniciais p0, p1  
- Tolerância configurável  
- Máximo de iterações  
- Retorno do zero aproximado + número de iterações  
- Mensagens de falha caso não converja  

---

## Arquitetura do Código

```
application/
│── main.py
│── ZetaFunction.py
│── GammaFunction.py
│── SecantMethod.py
```

Classes principais:

- **GammaFunction** — cálculo da função gama complexa via Lanczos  
- **ZetaFunction** — implementação da função Z(t)  
- **SecantMethod** — método da Secante do Burden  

---

## Como Rodar

No diretório raiz, execute:

```
python3 -m application.main
```
---

## Exemplo de Saída

```
============ TESTE : PARA 1000 ITERAÇÕES POR INTERVALO =============:
Falha no intervalo [24.51, 25.51]: Método da secante falhou: número máximo de iterações excedido.
Falha no intervalo [55.95, 56.95]: Método da secante falhou: número máximo de iterações excedido.

quantidade de zeros encontrados: 39

zero (1): t = 14.517919628262  |  interação = 5  |  intervalo usado = [13.63, 14.63]
zero (2): t = 20.654044969368  |  interação = 5  |  intervalo usado = [20.52, 21.52]
zero (3): t = 30.731877908492  |  interação = 6  |  intervalo usado = [29.92, 30.92]
zero (4): t = 32.688929806777  |  interação = 7  |  intervalo usado = [32.43, 33.43]
zero (5): t = 37.716482062397  |  interação = 6  |  intervalo usado = [37.08, 38.08]
zero (6): t = 40.758511514742  |  interação = 5  |  intervalo usado = [40.41, 41.41]
zero (7): t = 43.460371685047  |  interação = 6  |  intervalo usado = [42.83, 43.83]
zero (8): t = 47.824617076175  |  interação = 7  |  intervalo usado = [47.5, 48.5]
zero (9): t = 50.003418594753  |  interação = 6  |  intervalo usado = [49.27, 50.27]
zero (10): t = 52.794917256903  |  interação = 6  |  intervalo usado = [52.47, 53.47]
zero (11): t = 59.714786909054  |  interação = 7  |  intervalo usado = [58.85, 59.85]
zero (12): t = 60.531122079866  |  interação = 8  |  intervalo usado = [60.33, 61.33]
zero (13): t = 65.249966062619  |  interação = 7  |  intervalo usado = [64.61, 65.61]
zero (14): t = 66.924096320888  |  interação = 6  |  intervalo usado = [66.58, 67.58]
zero (15): t = 69.655450075643  |  interação = 6  |  intervalo usado = [68.55, 70.55]
zero (16): t = 71.991172219793  |  interação = 7  |  intervalo usado = [71.07, 73.07]
zero (17): t = 76.996342520215  |  interação = 9  |  intervalo usado = [74.7, 76.7]
zero (18): t = 76.996342520215  |  interação = 9  |  intervalo usado = [76.14, 78.14]
zero (19): t = 79.413402726706  |  interação = 7  |  intervalo usado = [78.34, 80.34]
zero (20): t = 82.830422391199  |  interação = 8  |  intervalo usado = [81.91, 83.91]
zero (21): t = 84.839475666237  |  interação = 6  |  intervalo usado = [83.74, 85.74]
zero (22): t = 84.839475666237  |  interação = 8  |  intervalo usado = [86.43, 88.43]
zero (23): t = 88.922035405135  |  interação = 9  |  intervalo usado = [87.81, 89.81]
zero (24): t = 92.392973917936  |  interação = 8  |  intervalo usado = [91.49, 93.49]
zero (25): t = 95.603079953053  |  interação = 7  |  intervalo usado = [93.65, 95.65]
zero (26): t = 94.933079300611  |  interação = 8  |  intervalo usado = [94.87, 96.87]
zero (27): t = 98.954057271397  |  interação = 6  |  intervalo usado = [97.83, 99.83]
zero (28): t = 101.458798150180  |  interação = 6  |  intervalo usado = [100.32, 102.32]
zero (29): t = 103.551961830706  |  interação = 7  |  intervalo usado = [102.73, 104.73]
zero (30): t = 105.633985258199  |  interação = 7  |  intervalo usado = [104.45, 106.45]
zero (31): t = 107.051776744682  |  interação = 10  |  intervalo usado = [106.17, 108.17]
zero (32): t = 111.616762961323  |  interação = 9  |  intervalo usado = [110.03, 112.03]
zero (33): t = 116.154328918512  |  interação = 11  |  intervalo usado = [110.87, 112.87]
zero (34): t = 114.413129594312  |  interação = 7  |  intervalo usado = [113.32, 115.32]
zero (35): t = 116.154328918512  |  interação = 7  |  intervalo usado = [115.23, 117.23]
zero (36): t = 118.843430799076  |  interação = 6  |  intervalo usado = [117.79, 119.79]
zero (37): t = 121.289016898366  |  interação = 10  |  intervalo usado = [120.37, 122.37]
zero (38): t = 124.171556376854  |  interação = 13  |  intervalo usado = [121.95, 123.95]
zero (39): t = 123.069524665729  |  interação = 9  |  intervalo usado = [123.26, 125.26]
```

Erros esperados:

- Intervalos sem mudança de sinal → secante falha  
- t muito pequeno → domínio inválido da Riemann–Siegel  
- Oscilações grandes → máximo de iterações excedido  

---

## Próximos Passos

- Melhorar precisão de θ(t)  
- Adicionar termos corretivos da fórmula de Riemann–Siegel  
- Criar gráficos de Z(t)  
- Comparar zeros encontrados com zeros tabelados   

---

## Referências

- Burden, Faires & Burden — Fundamentos de Análise Numérica (10ª ed.).  
- H. M. Edwards — Riemann’s Zeta Function.  
- Titchmarsh — The Theory of the Riemann Zeta Function.

