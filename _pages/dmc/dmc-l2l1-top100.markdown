---
permalink: /docs/dmc-l2l1-top100/
layout: single
classes: wide
sidebar:
  nav: "docs"
title:  "Differentially methylated CpG sites - L2 vs. L1 (Top 100)"
categories: dna-methylation dmc l2l1
datatable:
  id: dmcl3l1_top100
  nrow: 100
  nowrap: "Q-value"
---

## DMCs for L2:L1
We identified 27433 DMCs for L2:L1 when the following criteria were applied and L1 was used as control.
1. `abs(percentage methylation difference) >= 25%`
2. `Q-value < 0.01`

## Page links
- [What are DMCs?]({{ site.baseurl }}/docs/differentially-expressed-gene/){: .btn}
- [DMCs L3:L1 (top 100)]({{ site.baseurl }}/docs/dmc-l3l1-top100/){: .btn}
- [DMCs L2:L1 (full list)]({{ site.baseurl }}/docs/dmc-l2l1-full/){: .btn}
- [DMCs L3:L1 (full list)]({{ site.baseurl }}/docs/dmc-l3l1-full/){: .btn}

## Relevant Excel files
[Excel files (Downloads page)]({{ site.baseurl }}/docs/downloads/#13-excel-files-for-degs-dmcs-and-dmgs){: .btn} contain more information than the list presented here.

{% capture excel %}
- Dataset_03_CpG_L2L1.xlsx
- Dataset_05_DMC_Region_Gonad_L2L1.xlsx
{% endcapture %}

<div class="notice">
  {{ excel | markdownify }}
</div>

## List of the DMCs between L1 and L2 diets (top 100 by Q-value)

{% include datatable.html id=page.datatable.id
  data=site.data.dmc.dmcl2l1_top100 nrow=page.datatable.nrow
  nowrap=page.datatable.nowrap %}
