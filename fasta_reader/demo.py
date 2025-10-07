from reader import Seq, FastaReader


def demo_seq_class():
    """Демонстрация работы класса Seq"""
    print("=== ДЕМОНСТРАЦИЯ КЛАССА Seq ===")

    # Создаём тестовые последовательности
    protein_seq = Seq("sp|P12345|TEST_PROTEIN", "MSTAGKVIKCKAAVL")
    dna_seq = Seq("chr1:100-200", "ATCGATCGATCG")

    # Демонстрируем методы класса Seq
    print("1. Белковая последовательность:")
    print(protein_seq)
    print(f"   Длина: {len(protein_seq)}")
    print(f"   Алфавит: {protein_seq.get_alphabet()}")

    print("\n2. ДНК последовательность:")
    print(dna_seq)
    print(f"   Длина: {len(dna_seq)}")
    print(f"   Алфавит: {dna_seq.get_alphabet()}")


def demo_fasta_reader():
    """Демонстрация работы класса FastaReader"""
    print("\n" + "=" * 50)
    print("=== ДЕМОНСТРАЦИЯ КЛАССА FastaReader ===")

    # Создаём объект FastaReader (просто имя файла)
    reader = FastaReader("test_utf8.fasta")

    # Читаем и выводим все записи
    print("Записи из FASTA файла:")
    count = 0
    for i, record in enumerate(reader, 1):
        count += 1
        print(f"\n{i}. {record.header}")
        print(f"   Последовательность: {record.sequence}")
        print(f"   Длина: {len(record)}")
        print(f"   Алфавит: {record.get_alphabet()}")

    if count == 0:
        print("Не найдено ни одной записи!")


if __name__ == "__main__":
    demo_seq_class()
    demo_fasta_reader()