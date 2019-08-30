#!/bin/bash
#$ -S /bin/bash
#$ -j y
#$ -cwd
#$ -q phihost@phihost.local.net
#$ -pe openmp 40

for chr in {19..22}; do
python postSeqKit3.py allchroms_smallseq.fa_vs_chr"${chr}"_10xmatches.fa.txt allchroms_smallseq.fa_vs_chr"${chr}"_10xmatches.tsv ;
done