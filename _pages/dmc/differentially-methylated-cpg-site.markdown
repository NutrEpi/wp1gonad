---
permalink: /docs/differentially-methylated-cpg-site/
layout: single
sidebar:
  nav: "docs"
toc: true
toc_sticky: true
#comments: true
#share: true
title:  "What are DMCs?"
categories: summary dna-methylation dmc
---
DMC stands for differentially methylated CpG site. The difference of DNA methylation is statistically significant between treatment and control groups for each DMC.

## Treatment and control groups
We used three groups - L1, L2 and L3 diets - to calculate DMCs. L1 diet was used as control.

{% capture comps %}
- **L2:L1**: L2 vs. L1 with using L1 as control
- **L3:L1**: L3 vs. L1 with using L1 as control
{% endcapture %}

<div class="notice">
  <h4 class="no_toc">Data sets for differential expression analysis</h4>
  {{ comps | markdownify }}
</div>

See [Experimental feed]({{ site.baseurl }}/docs/project-summary/#experimental-feed){: .btn} for details about L1, L2 and L3 groups.

## Statistical calculation
We used [methylKit](https://bioconductor.org/packages/methylKit/){: .btn} to calculate methylation differences (%) and q-values between treatment and control groups. Positive methylation differences indicate hyper-methylation, whereas negative methylation differences indicate hypo-methylation based on the L1 DNA methylation. We used the following criteria to define our DEGs.

1. `abs(percentage methylation differences) >= 25%`
2. `Q-value < 0.01`

## Differentially methylated CpG sites
There are no noticeable differences between L2:L1 and L3:L1 as well as hypo- and hyper-methylation in terms of the number of DMCs.

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

## List of DMCs with locations and associated genes
- [List of DMCs - L2 vs. L1 (top 100)]({{ site.baseurl }}/docs/dmc-l2l1-top100/){: .btn}
- [List of DMCs - L3 vs. L1 (top 100)]({{ site.baseurl }}/docs/dmc-l3l1-top100/){: .btn}
- [List of DMCs - L2 vs. L1 (full list)]({{ site.baseurl }}/docs/dmc-l2l1-full/){: .btn}
- [List of DMCs - L3 vs. L1 (full list)]({{ site.baseurl }}/docs/dmc-l3l1-full/){: .btn}
- [Excel files (Downloads page)]({{ site.baseurl }}/docs/downloads/#9-excel-files-for-degs-dmcs-and-dmgs){: .btn}
