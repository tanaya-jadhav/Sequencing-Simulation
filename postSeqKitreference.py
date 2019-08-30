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


# def main(matchfile, outfasta):
def main():
    matchfile = ''
    sko = pd.read_csv(matchfile, sep='\t', header=0, index_col=None)
    sko = sko.sort_values(by=['start'])
    outputchr = matchfile.split('.')[0]
    # # outputpng = outputchr + '_NEWhist.png'
    # # outputdf = outputchr + '_NEWfrequency.tsv'
    reads = []
    smallseq = ''
    matchdict = {}
    for index, row in sko.iterrows():
        read = row['seqID']
        # print(read)
        if read not in reads:
            reads.append(read)
    #         counter = 1
            smallseq = ''
            match = str(row['matched']).upper()[-1]
            smallseq = smallseq + match
            matchdict[read] = smallseq
            # pattern = row['pattern']
            # matchdict[read] = (counter, pattern)
        else:
            # counter = counter + 1
            match = str(row['matched']).upper()[-1]
            smallseq = smallseq + match
            matchdict[read] = smallseq
            # pattern = row['pattern']
            # matchdict[read] = (counter, pattern)
        print(len(reads))
    print('small seq found')
    matches = pd.DataFrame.from_dict(matchdict, orient='index')
    print(matches)
    # matches.to_csv('allchroms_smallseq_vs_chr1_10xsmallseq.tsv', sep='\t', header=None)
    # f = pd.read_csv('allchroms_smallseq_vs_chr1_10xsmallseq.tsv', sep='\t', header=None)
    # print(f)
    # f = f.sort_values(by=[0])
    # print(f)
    #
    with open('chr1_smallseqnew2.fa', 'a') as o:
        for index, row in matches.iterrows():
            name = index
            seq = row[0]
            string = '>' + str(name) + '\n' + seq + '\n'
            o.write(string)

    # sslist = list(matches[0])

    # fl = []
    # for i in range(len(sslist)):
    #     freq = search(sslist, sslist[i])
    #     print(freq)
    #     fl.append(freq)
    # # print(fl)
    # ranges = ['0-5', '6-10', '11-15', '16-20', '21-25', '26-30', '31-35',
    #           '36-40', '41-45', '46-50', '51-55', '56-60', '61-65', '66-70',
    #           '71-75', '76-80', '81-85', '86-90', '91-95', '96-100']
    # rangedict = {}
    # for r in ranges:
    #     low = int(r.split('-')[0])
    #     high = int(r.split('-')[1])
    #     counter = 0
    #     for freq in fl:
    #         if freq >= low or freq <= high:
    #             counter = counter + 1
    #     rangedict[r] = counter

    # df = pd.DataFrame.from_dict(rangedict, orient='index')
    # df.sort_index(inplace=True)
    # df.to_csv(outputdf, sep='\t', header=None)
    # a = sns.distplot(fl, bins=100)
    # plt.savefig(outputpng)


if __name__ == '__main__':
    # matchfile = sys.argv[1]
    # outfasta = sys.argv[2]
    # main(matchfile, outfasta)
    main()