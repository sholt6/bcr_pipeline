configfile:
    "config.json"

SAMPLES, = glob_wildcards(config['fastq']+"/{id}_R1.fastq")

rule merge_reads:
    input:
        "Fastqs/{sample}_R1.fastq", sample=SAMPLES
    output:
        "Merged_Reads/{sample}_merged.fasta"
    shell:
        "usearch -fastq_mergepairs {input} -fastaout {output} "

rule mask_primers:
    input:
        "Merged_Reads/{sample}_merged.fasta", sample=SAMPLES
    output:
        "Masked_Reads/{sample}_masked.fasta"
    shell:
        "MaskPrimers.py align -s {input} -p {output}"
