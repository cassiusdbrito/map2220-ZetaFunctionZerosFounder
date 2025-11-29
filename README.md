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

## 🏗 Arquitetura do Código

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

## ▶Como Rodar

No diretório `application/`, execute:

```
python3 main.py
```

ou

```
py main.py
```

---

## Exemplo de Saída

```
============ TESTE : PARA 50 ITERAÇÕES =============:
zero (1): t = 14.517919628262  |  interação = 5
zero (2): t = 20.654044969368  |  interação = 6
zero (3): t = 32.688929806777  |  interação = 6

quantidade de zeros encontrados: 3
```

Erros esperados:

- Intervalos sem mudança de sinal → secante falha  
- t muito pequeno → domínio inválido da Riemann–Siegel  
- Oscilações grandes → máximo de iterações excedido  

---

## Restrições de Bibliotecas

Conforme instruções do professor:

### ✔ Permitido:
- math  
- cmath  
- time  
- datetime  
- os  
- numpy  
- matplotlib  

### Proibido:
- scipy  
- mpmath  
- qualquer biblioteca numérica avançada  

Por isso a função Gamma foi implementada manualmente.

---

## Próximos Passos

- Melhorar precisão de θ(t)  
- Adicionar termos corretivos da fórmula de Riemann–Siegel  
- Criar gráficos de Z(t)  
- Comparar zeros encontrados com zeros tabelados  
- Criar um scanner automático de zeros  

---

## Referências

- Burden, Faires & Burden — Fundamentos de Análise Numérica (10ª ed.).  
- H. M. Edwards — Riemann’s Zeta Function.  
- Titchmarsh — The Theory of the Riemann Zeta Function.

