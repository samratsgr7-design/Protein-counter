# Protein Counter - Biotechnology Tool 🧬
# Created by samratsgr7-design

def analyze_protein(sequence):
    sequence = sequence.upper().replace(" ", "")
    length = len(sequence)
    
    # 20 standard amino acids
    amino_acids = "ACDEFGHIKLMNPQRSTVWY"
    
    print(f"Protein Sequence: {sequence}")
    print(f"Length: {length} amino acids")
    print("\nAmino Acid Composition:")
    
    for aa in amino_acids:
        count = sequence.count(aa)
        if count > 0:
            percent = (count / length) * 100
            print(f"{aa}: {count} ({percent:.1f}%)")
    
    # Hydrophobic check
    hydrophobic = sum(sequence.count(a) for a in "AILMFWVY")
    print(f"\nHydrophobic AAs: {hydrophobic}")

# Example - Insulin fragment
protein = "GIVEQCCTSICSLYQLENYCN"
analyze_protein(protein)
