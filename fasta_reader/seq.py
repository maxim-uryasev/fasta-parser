class Seq:
    protein_alphabet = set('ACDEFGHIKLMNPQRSTVWY')
    nuc_alphabet = set('ACGT')

    def __init__(self, sequence: str, inf: str):
        self.sequence = sequence.strip().replace(" ", "")
        self.inf = inf

    def __str__(self):
        return self.sequence

    def __len__(self):
        return len(self.sequence)

    def alph(self):
        sequp = self.sequence.upper()
        if all(x in self.protein_alphabet for x in sequp):
            return 'protein'
        if all(x in self.nuc_alphabet for x in sequp):
            return 'nuc'
        else:
            return 'unknown'