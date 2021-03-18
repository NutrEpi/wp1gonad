---
permalink: /docs/dna-methylation/
layout: single
sidebar:
  nav: "docs"
toc: true
toc_sticky: true
#comments: true
#share: true
title:  "Summary of DNA methylation analysis"
categories: summary dna-methylation dmc dmg
---
A brief summary of our DNA methylation analysis.

## RRBS

We used RRBS (reduced representation bisulfite sequencing) to analyse the DNA methylation profiles affected by our experimental feed with different micronutrient compositions. RRBS utilises restriction enzymes to target CpG rich regions in the genome. We used two different enzymes for our RRBS analysis.

{% capture enzymes %}
1. MspI (recognition sequence : `5' CCGG`)
2. TaqI (recognition sequence : `5' TCGA`)
{% endcapture %}

<div class="notice">
  <h4 class="no_toc">Restriction enzymes used for RRBS</h4>
  {{ enzymes | markdownify }}
</div>

## RRBS samples
We collected 9 male gonad samples at the final harvest stage for RRBS sequencing.

{% capture feed_groups %}
- **L1 diet**: 3 samples
- **L2 diet**: 3 samples
- **L3 diet**: 3 samples
{% endcapture %}

<div class="notice">
  <h4 class="no_toc">The number of samples for each group</h4>
  {{ feed_groups | markdownify }}
</div>

{% include datatable_sortonly.html id='table_rrbs'
  data=site.data.dna.rrbs_samples nrow=9 %}

## Definition of genomic regions
Functions of DNA methylation can be different depending on the types of regions where methylation occurs.
We split the genome into seven different regions for our RRBS analysis.

{% capture regions %}
1. Exon
2. Intron
3. P250 (proximal promoter)
4. P1K (promoter)
5. P5K (distal promoter)
6. Flanks (potential enhancer region)
7. IGR (intergenic region)
{% endcapture %}

<div class="notice">
  <h4 class="no_toc">Genomic regions for RRBS read mapping</h4>
  {{ regions | markdownify }}
</div>

<figure>
  <img src="{{ site.baseurl }}/assets/images/dna/genomic_regions_gonad.svg" alt="Genomic regions for RRBS read alignment" >
  <figcaption>Definition of genomic regions for RRBS read alignment.</figcaption>
</figure>

## Bioinformatics pipelne for RRBS
We used various bioinformatics algorithms and methods to analyse our RRBS samples.
The following tools were those we used in our main RRBS pipeline.
- [FastQC](https://cutadapt.readthedocs.io/en/stable/){: .btn} (quality control)
- [Trim Galore!](https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/){: .btn} (adapter trimming)
- [MultiQC](https://multiqc.info/){: .btn} (quality control report)
- [Bismark](https://www.bioinformatics.babraham.ac.uk/projects/bismark/){: .btn} (read alignment)
- [methylKit](https://bioconductor.org/packages/methylKit/){: .btn} (differential methylation analysis)

## Results
### Overall diet effect
Clustering analysis showed no clear overall diet effects on the male gonad samples.
<figure>
    <img src="{{ site.baseurl }}/assets/images/dna/rrbs_pca_gonad_p.svg" alt="PCA bi-blot for RRBS samples" >
    <figcaption>PCA (principal component analysis) bi-plot for clustering the 9 RRBS samples.</figcaption>
</figure>

### Differentially methylated CpG sites
There were no noticeable differences between L2:L1 and L3:L1 as well as hypo- and hyper-methylation in terms of the number of DMCs.

{% capture dmcs %}
- **L2 vs. L1**: 27433 DMCs
- **L3 vs. L1**: 26995 DMCs
{% endcapture %}

<div class="notice">
  <h4 class="no_toc">Identified DMCs for L2:L1 and L3:L1</h4>
  {{ dmcs | markdownify }}
</div>

<figure>
    <img src="{{ site.baseurl }}/assets/images/dna/dmc_gonad.png" alt="Violin plots of DMCs">
    <figcaption>Violin plots of DMCs.</figcaption>
</figure>

See [What are DMCs?]({{ site.baseurl }}/docs/differentially-methylated-cpg-site/){: .btn} for more details about DMCs.

### Significantly affected biological pathways
[ORA](https://doi.org/10.1093/bioinformatics/bth456){: .btn} (over representation analysis) on [KEGG](https://www.genome.jp/kegg/){: .btn} (Kyoto Encyclopedia of Genes and Genomes) pathways showed that micronutrient supplement significantly affected DNA methylation profiles in various pathways mainly through DNA methylation in their gene bodies.

{% include table.html id='table_rrbs_ora' data=site.data.dna.rrbs_ora
   caption='Enriched KEGG pathways by ORA (over representation analysis).' %}

## Page links
*Overview*
- [Project summary]({{ site.baseurl }}/docs/project-summary/){: .btn}
- [Gene expression]({{ site.baseurl }}/docs/gene-expression/){: .btn}

*DMC: differentially methylated CpG site*
- [What are DMCs?]({{ site.baseurl }}/docs/differentially-expressed-gene/){: .btn}
- [DMCs L2:L1 (top 100)]({{ site.baseurl }}/docs/dmc-l2l1-top100/){: .btn}
- [DMCs L3:L1 (top 100)]({{ site.baseurl }}/docs/dmc-l3l1-top100/){: .btn}
- [DMCs L2:L1 (full list)]({{ site.baseurl }}/docs/dmc-l2l1-full/){: .btn}
- [DMCs L3:L1 (full list)]({{ site.baseurl }}/docs/dmc-l3l1-full/){: .btn}

*DMG: differentially methylated gene*
- [What are DMGs?]({{ site.baseurl }}/docs/differentially-expressed-gene/){: .btn}
- [DMGs L2:L1 (promoter)]({{ site.baseurl }}/docs/dmg-l2l1-multi-dmcs-promoter/){: .btn}
- [DMGs L3:L1 (promoter)]({{ site.baseurl }}/docs/dmg-l3l1-multi-dmcs-promoter/){: .btn}
- [DMGs L2:L1 (full list)]({{ site.baseurl }}/docs/dmg-l2l1-full/){: .btn}
- [DMGs L3:L1 (full list)]({{ site.baseurl }}/docs/dmg-l3l1-full/){: .btn}
