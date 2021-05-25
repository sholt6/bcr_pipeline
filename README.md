Described here is a Snakemake pipeline written to assemble paired-end read data of B cell receptors (BCR), mask the primer sequences, and graph the usage of each primer.
In characterising the antibody profiles of individuals, pipelines such as this are useful for taking the raw experimental data through to a set of assembled B cell receptor sequences.


# Running The Pipeline
The pipeline is available in GitHub:
 * https://github.com/sholt6/bcr_pipeline

Please ensure you have conda and snakemake installed on your system. Both of these are covered in the Snakemake documentation:
 * https://snakemake.readthedocs.io/en/stable/getting_started/installation.html

Ensure usearch is available at your command line as command `usearch`. You can download the appropriate version for your OS at:
 * https://www.drive5.com/usearch/download.html

## To download and run:

1. git clone https://github.com/sholt6/bcr_pipeline.git
2. cd bcr_pipeline
3. conda env create -f alchemab_test.yml -n alchemab_test
4. conda activate alchemab_test
5. snakemake plots/SE-0000025_primer_usage.svg
