# Automated VUS Prioritization Pipeline

A scalable, disease-agnostic computational framework for the systematic triage and structural evaluation of Variants of Uncertain Significance (VUS). 

This pipeline automates the extraction, annotation, filtering, and structural mapping of missense VUS from ClinVar. By combining population genetics, *in silico* pathogenicity predictors, and AI-driven structural biology (AlphaFold/ESMFold), it isolates highly probable pathogenic candidates and maps them to their 3D physical vulnerabilities (e.g., domain interfaces, calcium-binding pockets, disulfide networks) to generate immediate, publication-ready hypotheses for functional validation.

## 🧬 Key Features
* **Automated VCF Parsing:** Extracts gene-specific, anchored VUS records directly from massive ClinVar GRCh38 release files.
* **Transcript-Aware API Annotation:** Leverages the Ensembl VEP REST API via robust batching to fetch SIFT, PolyPhen-2, and gnomAD frequencies. Intelligently prioritizes canonical transcripts to survive complex alternative splicing and nonsense-mediated decay (NMD) networks.
* **Stringent Pathogenicity Filtering:** Employs mathematically strict thresholds to isolate ultra-rare, structurally damaging variants (e.g., gnomAD AF < 1×10⁻⁴, SIFT < 0.05, PolyPhen-2 > 0.90).
* **Automated Domain Mapping:** Cross-references surviving genomic coordinates against canonical UniProt sequences to cluster mutations functionally.
* **AI Structural Integration:** Automatically fetches pre-computed high-resolution structures from the AlphaFold Protein Structure Database, or queries the Meta ESMFold API for *de novo* modeling when massive proteins (like FBN1) exceed public database length limits.

## 📂 Repository Structure
* `/scripts` — Contains the modular Python and Bash scripts driving the pipeline.
  * `run_pipeline.sh`: The master execution script.
  * `annotate_gene.py`: Handles batch Ensembl API requests with automatic retry/backoff logic.
  * `rank_variants.py`: Applies joint clinical and statistical filtering.
  * `map_domains.py`: Assigns biological domain context to passing candidates.
  * `download_structure.py` / `fold_fbn1.py`: Manages structural modeling via AlphaFold or ESMFold.
* `/FBN1_Results` — Pipeline outputs and ray-traced PyMOL figures for *FBN1* (Marfan Syndrome).
* `/MYBPC3_Results` — Pipeline outputs for *MYBPC3* (Hypertrophic Cardiomyopathy) *(In Progress)*.
* *Note: The initial LDLR (Familial Hypercholesterolemia) baseline implementation remains archived in its [original repository](https://github.com/mubeeen1/LDLR-Variant-Prioritization).*

## 🚀 Quick Start & Usage

### Prerequisites
* Python 3.8+ (`pandas`, `requests`)
* Standard Bash utilities (`grep`, `awk`, `sed`)
* **PyMOL** (for rendering publication-quality structural figures)
* A local copy of the ClinVar VCF (`clinvar.vcf.gz` and its `.tbi` index). *Note: Added to `.gitignore` due to size constraints.*

### Execution
The pipeline is fully automated through a single shell command. It requires four positional arguments:
1. `VCF File`
2. `Gene Symbol`
3. `Chromosome`
4. `UniProt ID`

**Example (Fibrillin-1 / Marfan Syndrome):**
```bash
./run_pipeline.sh clinvar.vcf.gz FBN1 15 P35555
