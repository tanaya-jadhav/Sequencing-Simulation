import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys


def search(arr, s):
    counter = 0
    for j in range(len(arr)):

        # checking if string given in query
        # is present in the given string.
        # If present, increase times
        if (s == (arr[j])):
            counter += 1

    return counter


def main(matchfile, outfasta):
# def main():
#     matchfile = 'chr1_10xreads.fa_vs_tag.fa.txt'
    sko = pd.read_csv(matchfile, sep='\t', header=0, index_col=None)
    # print(sko.head(10))
    sko = sko.sort_values(by=['seqID', 'start'])
    # print(sko.head(10))
    # outputchr = matchfile.split('.')[0].split('r')[0]
    reads = []
    smallseq = ''
    matchdict = {}
    for index, row in sko.iterrows():
        read = row['seqID']
        # print(read)
        if read not in reads:
            reads.append(read)
            smallseq = ''
            match = str(row['matched']).upper()[-1]
            smallseq = smallseq + match
            matchdict[read] = smallseq
        else:
            match = str(row['matched']).upper()[-1]
            smallseq = smallseq + match
            matchdict[read] = smallseq
        # print(len(reads))
    print('small seq found')
    matches = pd.DataFrame.from_dict(matchdict, orient='index')
    # print(matches)
    # matches.to_csv('chr1_10xmatches.tsv', sep='\t', header=None)
    # f = pd.read_csv('allchroms_smallseq_vs_chr1_10xsmallseq.tsv', sep='\t', header=None)
    # print(f)
    # f = f.sort_values(by=[0])
    # print(f)
    #
    with open(outfasta, 'a') as o:
        for index, row in matches.iterrows():
            name = index
            seq = row[0]
            string = '>' + str(name) + '\n' + seq + '\n'
            o.write(string)


if __name__ == '__main__':
    matchfile = sys.argv[1]
    outfasta = sys.argv[2]
    main(matchfile, outfasta)
    # main()