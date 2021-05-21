import matplotlib
import matplotlib.pyplot as plt

experiment_name = snakemake.input[0]
experiment_name = experiment_name[14:]
experiment_name = experiment_name[:-18]

primer_names = []
primer_counts = []

with open(snakemake.input[0], 'r') as usage_file:
    for line in usage_file:
        line = line.split(':')
        primer_names.append(line[0])
        primer_counts.append(int(line[1]))

x_positions = [i for i, _ in enumerate(primer_names)]

plt.bar(x_positions, primer_counts)
plt.xlabel("Primer Name")
plt.ylabel("Usage Count")
plt.title("Total Usages Of Each Primer In Sample %s" % experiment_name)

plt.xticks(x_positions, primer_names)

plt.savefig(snakemake.output[0])
