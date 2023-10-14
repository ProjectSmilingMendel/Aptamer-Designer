#!/bin/python3
import random

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

Amino_acids = [ "Ala" , "Cys" , "Asp" , "Glu" , "Phe" , "Gly" , "His" , "Ile" , "Lys" , "Leu" , "Met" , "Asn" , "Pro" , "Gln" , "Arg" , "Ser" , "Thr" , "Val" , "Trp" , "Tyr" ]

a_ac =        [ "A"   , "C"   , "D"   , "E"   , "F"   , "G"   , "H"   ,  "I"  , "K"   , "L"   , "M"   , "N"   , "P"   , "Q"   , "R"   , "S"   , "T"   , "V"   , "W"   , "Y" ]
smile_dict = {
    'A': 'C[C@@H](C(=O)[O])[NH3]',
    'R': 'NC(CCCNC(N)=[NH2])C([O])=O',
    'N': 'O=C(N)C[C@H]([NH3])C(=O)[O]',
    'D': 'C(C(C(=O)[O])[NH3])C(=O)O',
    'C': 'C([C@@H](C(=O)[O])[NH3])S',
    'E': 'C(CC(=O)O)C(C(=O)[O])[NH3]',
    'Q': 'O=C(N)CCC([NH3])C(=O)[O]',
    'G': 'C(C(=O)[O])[NH3]',
    'H': 'O=C([C@H](CC1=CNC=N1)[NH3])[O]',
    'I': 'CC[C@H](C)[C@@H](C(=O)[O])[NH3]',
    'L': 'CC(C)C[C@@H](C(=O)[O])[NH3]',
    'K': 'C(CC[NH3])C[C@@H](C(=O)[O])N',
    'M': 'CSCC[C@H]([NH3])C(=O)[O]',
    'F': '[NH3][C@@H](CC1=CC=CC=C1)C([O])=O',
    'P': '[O]C(=O)[C@H](CCC2)[NH2]2',
    'S': 'C([C@@H](C(=O)[O])[NH3])O',
    'T': 'C[C@H]([C@@H](C(=O)[O])[NH3])O',
    'W': 'c1[nH]c2ccccc2c1C[C@H]([NH3])C(=O)[O]',
    'Y': '[NH3][C@@H](Cc1ccc(O)cc1)C([O])=O',
    'V': 'CC(C)[C@@H](C(=O)[O])[NH3]' 
        }
peptide_length = random.randint(1,100)
a = ""
for i in range(6,peptide_length) :
    a= a+random.choice(a_ac)
b=""
for i in a:
    b = b + smile_dict[i]
print(b)

#for i in smile_dict:
    #print(smile_dict[i])

#for i in a:
 #   print(i, smile_dict[i])





