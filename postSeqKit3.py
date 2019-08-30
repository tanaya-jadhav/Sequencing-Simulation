import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
import sys

def main(matchfile, outfasta):
# def main():
    # matchfile = 'allchroms_smallseq.fa_vs_chr1_10xmatches.fa.txt'
    sko = pd.read_csv(matchfile, sep='\t', header=0, index_col=None)
    sko = sko.sort_values(by=['patternName', 'seqID', 'start'])
    reads = []
    matchdict = {}
    for index, row in sko.iterrows():
        read = row['patternName']
        # print(read)
        if read not in reads:
            chroms = []
            reads.append(read)
            counter = 1
            pattern = row['pattern']
            chrom = row['seqID']
            chroms.append(chrom)
            matchdict[read] = (chroms, counter, pattern)
        else:
            counter = counter + 1
            pattern = row['pattern']
            chrom = row['seqID']
            if chrom not in chroms:
                chroms.append(chrom)
            matchdict[read] = (chroms, counter, pattern)
        # print(len(reads))
    # print('small seq found')
    matches = pd.DataFrame.from_dict(matchdict, orient='index')

    # outdf = 'allchroms_smallseq_vs_chr1_10xmatches.tsv'
    matches.to_csv(outdf, sep='\t', header=None)


if __name__ == '__main__':
    matchfile = sys.argv[1]
    outdf = sys.argv[2]
    main(matchfile, outdf)
    # main()