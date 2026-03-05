import math

def T(n):
    if n == 1:
        return 1
    return 2 * T(n // 2) + n

def main():
    input_sizes = [2, 4, 8, 16, 32, 64]
    results = []

    results.append("n\tT(n)\tn*log2(n)")
    results.append("----------------------------------")

    for n in input_sizes:
        value = T(n)
        theoretical = int(n * math.log2(n))
        results.append(f"{n}\t{value}\t{theoretical}")

    for line in results:
        print(line)

    with open("recursion_tree_results.txt", "w") as f:
        for line in results:
            f.write(line + "\n")

    print("\nResults saved to recursion_tree_results.txt")

if __name__ == "__main__":
    main()