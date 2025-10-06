class Seq:
    """Класс для работы с последовательностями FASTA"""

    def __init__(self, header, sequence):
        self.header = header
        self.sequence = sequence

    def __str__(self):
        return f">{self.header}\n{self.sequence}"

    def __len__(self):
        return len(self.sequence)

    def get_alphabet(self):
        nucleotides = set('ATCGUNatcgun')
        protein = set('ACDEFGHIKLMNPQRSTVWYacdefghiklmnpqrstvwy')
        seq_chars = set(self.sequence)

        if seq_chars.issubset(nucleotides):
            return "nucleotide"
        elif seq_chars.issubset(protein):
            return "protein"
        else:
            return "unknown"


class FastaReader:
    """Класс для чтения FASTA файлов"""

    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        with open(self.filename, 'r') as file:
            header = ""
            sequence = ""

            for line in file:
                line = line.strip()
                if line.startswith('>'):
                    if header:
                        yield Seq(header, sequence)
                    header = line[1:]
                    sequence = ""
                else:
                    sequence += line

            if header:
                yield Seq(header, sequence)


def main():
    reader = FastaReader(r"C:\Users\Honor\Desktop\fasta_project\test.fasta.txt")

    print("Чтение FASTA файла:")
    for i, seq in enumerate(reader, 1):
        print(f"\nЗапись {i}:")
        print(f"Заголовок: {seq.header}")
        print(f"Длина: {len(seq)}")
        print(f"Алфавит: {seq.get_alphabet()}")
        print(f"Последовательность: {seq.sequence}")


if __name__ == "__main__":
    main()



