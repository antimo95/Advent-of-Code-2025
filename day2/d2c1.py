"""#Advent Of Code | DAY 2 | Code 1"""

def is_invalid_id(n: int) -> bool:
    s = str(n)  # converte il numero in stringa
    # Deve avere lunghezza pari
    if len(s) % 2 != 0: # se la lunghezza è dispari => non può essere invalido
        return False
    mid = len(s) // 2 # calcola la metà della lunghezza

    # confronta le due stringhe e ritorna il risultato
    if s[:mid] == s[mid:]:
        return True
    else:
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

