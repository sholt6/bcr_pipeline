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

rule mask_v_primers:
    input:
        reads="Merged_Reads/{sample}_merged.fasta", sample=SAMPLES,
        primers="Primers/v_primers.fasta"
    output:
        "Masked_Reads/{sample}_v_masked.fasta"
    shell:
        "MaskPrimers.py align -s {input.reads} "
        "-p {input.primers} -o {output} "
        "--revpr --mode mask "

rule mask_c_primers:
    input:
        reads="Masked_Reads/{sample}_v_masked.fasta",
        primers="Primers/c_primers.fasta"
    output:
        "Masked_Reads/{sample}_vc_masked.fasta"
    shell:
        "MaskPrimers.py align -s {input.reads} "
        "-p {input.primers} -o {output} "
        "--revpr --mode mask "

rule count_primers:
    input:
        "Masked_Reads/{sample}_vc_masked.fasta"
    output:
        "{sample}_primer_counts.txt"
    script:
        "primer_counts.py -f {input} -o {output} "
