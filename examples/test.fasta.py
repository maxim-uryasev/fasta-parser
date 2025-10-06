from fasta_reader import FastaReader
import sys
import os
def main():
    reader = FastaReader(r'C:\Users\Honor\Desktop\fasta_project\examples\GCA_000006945.2_ASM694v2_genomic.fna')
    if not reader.check():
        return
    for seq in reader.read():
        print(f'title: {seq.inf}')
        print(f'seq: {seq}')
        print(f'length: {len(seq)}')
        print(f'type: {seq.alph()}')

main()