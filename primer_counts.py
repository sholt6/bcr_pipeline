

import argparse
import re

def argument_parse():
    parser = argparse.ArgumentParser(description='''
        Count primer occurrences in PRESTO processed file
        ''')
    parser.add_argument('-f', '--fasta', type=str,
                        help='input FASTA file')
    parser.add_argument('-o', '--outfile', type=str,
                        help='output tsv')
    args = parser.parse_args()
    return args

def get_id_content(line):
    if line[0] == '>':
        content = line.split('|')
        return content
    else:
        return None

def get_primers(id_content):
    primers_regex = re.compile(r'PRIMER=')
    for entry in id_content:
        if re.match(primers_regex, entry):
            primer_section = entry

    primer_text = primer_section[7:]
    primer_text = primer_text.rstrip()
    primers = primer_text.split(',')
    
    return primers

def main(arguments):

    fasta_name = arguments.fasta
    outfile_name = arguments.outfile
    primer_counts = {}

    with open(fasta_name, 'r') as fasta_file:
        for line in fasta_file:
            id_content = get_id_content(line)
            if id_content:
                primers = get_primers(id_content)
                for primer in primers:
                    if primer in primer_counts.keys():
                        primer_counts[primer] += 1
                    else:
                        primer_counts[primer] = 1

    with open(outfile_name, 'w') as outfile:
        for primer in primer_counts.keys():
            outfile.write("%s: %s\n" % (primer, primer_counts[primer]))

            


if __name__ == '__main__':
    arguments = argument_parse()
    main(arguments)
