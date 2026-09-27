import requests

print("1. Fetching FBN1 Sequence from UniProt...")
uniprot_url = "https://rest.uniprot.org/uniprotkb/P35555.fasta"
response = requests.get(uniprot_url)
fasta_lines = response.text.strip().split('\n')
full_sequence = "".join(fasta_lines[1:])

# Extract exactly residues 1820 to 2050 (0-indexed so 1819:2050)
target_seq = full_sequence[1819:2050]
print(f"Extracted {len(target_seq)} amino acids for cbEGF domains 30-35.")

print("2. Folding sequence in real-time via Meta ESMFold API...")
esm_url = "https://api.esmatlas.com/foldSequence/v1/pdb/"
esm_response = requests.post(esm_url, data=target_seq)

if esm_response.ok:
    with open("FBN1_ESMFold_Target.pdb", "w") as f:
        f.write(esm_response.text)
    print("Success! Saved true structural model as FBN1_ESMFold_Target.pdb")
else:
    print("Error folding protein.")
