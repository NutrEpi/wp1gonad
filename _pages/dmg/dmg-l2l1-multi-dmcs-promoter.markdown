---
permalink: /docs/dmg-l2l1-multi-dmcs-promoter/
layout: single
classes: wide
sidebar:
  nav: "docs"
title:  "Differentially methylated genes - L2 vs. L1 (promoter)"
categories: dna-methylation dmg l2l1
datatable:
  id: dmgl3l1_p2
  nrow: 289
---

## DMGs for L2:L1
We identified 9774 DMGs for L2:L1. We defined DMGs as the genes that required the following conditions.
1. A gene has at least one DMC in its gene body, promoter or flanking region.
2. Only the DMCs for L2:L1 were considered

## Page links
- [What are DMGs?]({{ site.baseurl }}/docs/differentially-expressed-gene/){: .btn}
- [DMGs L3:L1]({{ site.baseurl }}/docs/dmg-l3l1/){: .btn}

## Relevant Excel files
[Excel files (Downloads page)]({{ site.baseurl }}/docs/downloads/#9-excel-files-for-degs-dmcs-and-dmgs){: .btn} contain more information than the list presented here.

{% capture excel %}
- Dataset_07_DMG_L2L1.xlsx
{% endcapture %}

<div class="notice">
  {{ excel | markdownify }}
</div>

## List of the DMGs between L1 and L2 diets

<p class="notice--success">
<strong>NOTE</strong>: the list contains the DMGs that have at least two DMCs in their promoter region.
</p>

{% include datatable.html id=page.datatable.id
  data=site.data.dmg.dmgl2l1_p2 nrow=page.datatable.nrow
  nowrap=page.datatable.nowrap %}
