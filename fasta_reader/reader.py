class Seq:
    """Класс для работы с последовательностями FASTA"""

    def __init__(self, header, sequence):
        self.header = header
        self.sequence = sequence

    def __str__(self):
        return f">{self.header}\n{self.sequence}"

    def __repr__(self):
        return f"Seq(header='{self.header}', sequence='{self.sequence[:20]}...')"

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
        """Генератор для чтения больших файлов"""
        with open(self.filename, 'r', encoding='utf-8') as file:
            header = ""
            sequence = ""

            for line in file:
                line = line.strip()
                if not line:
                    continue
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
    reader = FastaReader('test_utf8.fasta')

    print("Чтение FASTA файла:")
    for i, seq in enumerate(reader, 1):
        print(f"\nЗапись {i}:")
        print(f"Заголовок: {seq.header}")
        print(f"Длина: {len(seq)}")
        print(f"Алфавит: {seq.get_alphabet()}")
        print(f"Последовательность: {seq.sequence}")


if __name__ == "__main__":
    main()