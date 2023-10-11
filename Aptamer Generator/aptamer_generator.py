#!/bin/python3
import random
Amino_acids = [ "Ala" , "Cys" , "Asp" , "Glu" , "Phe" , "Gly" , "His" , "Ile" , "Lys" , "Leu" , "Met" , "Asn" , "Pro" , "Gln" , "Arg" , "Ser" , "Thr" , "Val" , "Trp" , "Tyr" ]

A_ac = [ "A" , "C" , "D" , "E" , "F" , "G" , "H" , "I" , "K" , "L" , "M" , "N" , "P" , "Q" , "R" , "S" , "T" , "V" , "W" , "Y" ]

smile_dict = {
    'Ala': 'C[C@@H](C(=O)O)N',
    'Arg': 'C(C[C@@H](C(=O)O)N)CNC(=N)N',
    'Asn ': 'O=C(N)C[C@H](N)C(=O)O',
    'Asp ': 'C([C@@H](C(=O)O)N)C(=O)O',
    'Cys ': 'C([C@@H](C(=O)O)N)S',
    'Glu': 'C(CC(=O)O)[C@@H](C(=O)O)N',
    'Gln ': 'O=C(N)CCC(N)C(=O)O',
    'Gly': 'C(C(=O)O)N',
    'His ': 'O=C([C@H](CC1=CNC=N1)N)O',
    'Ile': 'CC[C@H](C)[C@@H](C(=O)O)N',
    'Leu': 'CC(C)C[C@@H](C(=O)O)N',
    'Lys': 'C(CCN)C[C@@H](C(=O)O)N',
    'Met ': 'CSCC[C@H](N)C(=O)O',
    'Phe ': ' c1ccc(cc1)C[C@@H](C(=O)O)N',
    'Pro': 'C1C[C@H](NC1)C(=O)O',
    'Ser': 'C([C@@H](C(=O)O)N)O',
    'Thr': 'C[C@H]([C@@H](C(=O)O)N)O',
    'Trp': 'c1[nH]c2ccccc2c1C[C@H](N)C(=O)O',
    'Tyr': 'N[C@@H](Cc1ccc(O)cc1)C(O)=O',
    'Val': 'CC(C)[C@@H](C(=O)O)N' 
        }

smile_dict = {
    'Ala': 'C[C@@H](C(=O)O)N',
    'Arg': 'C(C[C@@H](C(=O)O)N)CNC(=N)N',
    'Asn ': 'O=C(N)C[C@H](N)C(=O)O',
    'Asp ': 'C([C@@H](C(=O)O)N)C(=O)O',
    'Cys ': 'C([C@@H](C(=O)O)N)S',
    'Glu': 'C(CC(=O)O)[C@@H](C(=O)O)N',
    'Gln ': 'O=C(N)CCC(N)C(=O)O',
    'Gly': 'C(C(=O)O)N',
    'His ': 'O=C([C@H](CC1=CNC=N1)N)O',
    'Ile': 'CC[C@H](C)[C@@H](C(=O)O)N',
    'Leu': 'CC(C)C[C@@H](C(=O)O)N',
    'Lys': 'C(CCN)C[C@@H](C(=O)O)N',
    'Met ': 'CSCC[C@H](N)C(=O)O',
    'Phe ': ' c1ccc(cc1)C[C@@H](C(=O)O)N',
    'Pro': 'C1C[C@H](NC1)C(=O)O',
    'Ser': 'C([C@@H](C(=O)O)N)O',
    'Thr': 'C[C@H]([C@@H](C(=O)O)N)O',
    'Trp': 'c1[nH]c2ccccc2c1C[C@H](N)C(=O)O',
    'Tyr': 'N[C@@H](Cc1ccc(O)cc1)C(O)=O',
    'Val': 'CC(C)[C@@H](C(=O)O)N' 
        }
peptide_length = random.randint(1,100)
a = ""
for i in range(3,peptide_length) :
        a= a+random.choice(A_ac)
print(a)
