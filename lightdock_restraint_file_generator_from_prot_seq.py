
amino_acids_dictionary = { 'A': 'ALA',
                           'R': 'ARG',
                           'N': 'ASN',
                           'D':'ASP',
                           'C': 'CYS',
                           'Q':'GLN',
                           'G':'GLY',
                           'E':'GLU',
                           'H': 'HIS',
                           'I': 'ILE',
                           'L': 'LEU',
                           'K': 'LYS',
                           'M': 'MET',
                           'F':'PHE',
                           'P':'PRO',
                           'S':'SER',
                           'T':'THR',
                           'W':'TRP',
                           'Y':'TYR',
                           'V':'VAL'
}

seq = "VVVEIGKVTGSVGTTVEIPVYFRGVPSKGIANCDFVFRYDPNVLEIIGIDPGDIIVDPNPTK" \
      "SFDTAIYPDRKIIVFLFAEDSGTGAYAITKDGVFAKIRATVKSSAPGYITFDEVGGFADNDLVEQKVSFI" \
      "DGGVNV"
m=219
for n in seq:

    print('L A.'+ amino_acids_dictionary[n] + '.' + str(m))
    m+=1