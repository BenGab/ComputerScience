def calculate_pi(n_terms: int) -> float:
    numarator: float = 4.0
    denomiator: float = 1.0
    operand: float = 1.0
    pi: float = 0.0
    for _ in range(n_terms):
        pi += operand * (numarator / denomiator)
        denomiator += 2.0
        operand *= -1.0
    return pi

if __name__ == "__main__":
    print(calculate_pi(10000))