[Seq]
- header: str
- sequence: str
+ __str__()
+ __len__()
+ get_alphabet()

[FastaReader]
- filename: str
+ __iter__()
+ is_valid_fasta()

[Seq] <- [FastaReader]S