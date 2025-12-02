"""#Advent Of Code | DAY 2 | Code 2"""

def is_invalid_id(n: int) -> bool:
    s = str(n)
    length = len(s)
    # prova tutte le possibili lunghezze di blocco (hai almeno 2 ripetizioni)
    for block_size in range(1, length // 2 + 1):
        if length % block_size == 0:  # deve dividere esattamente
            # Estraggo il blocco
            block = s[:block_size]
            # Ripeto il blocco per coprire tutta la lunghezza della stringa
            if block * (length // block_size) == s:
                return True
    return False

def sum_invalid_ids_from_file(filename: str) -> int:
    with open(filename, "r") as f:
        input_line = f.read().strip()
    total = 0
    ranges = input_line.split(",") # ottengo una lista di sottostringhe ("intervalli")
    for r in ranges:
        start, end = map(int, r.split("-")) # 1123-1345 => start = 1123 | end = 1345
        for n in range(start, end + 1):
            if is_invalid_id(n):
                total += n
    return total

# 🔹 Uso
if __name__ == "__main__":
    result = sum_invalid_ids_from_file("inpunt.txt")
    print("Somma totale degli ID invalidi:", result)

