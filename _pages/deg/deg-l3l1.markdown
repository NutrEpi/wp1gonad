---
permalink: /docs/deg-l3l1/
layout: single
classes: wide
sidebar:
  nav: "docs"
title:  "Differentially expressed genes - L3 vs. L1"
categories: gene-expression deg l3l1
datatable:
  id: degl3l1
  nrow: 97
  nowrap: "Adj p-val"
---

## DEGs for L3:L1
We identified 97 DEGs for L3:L1 when the following criteria were applied and L1 was used as control.
1. `abs(LFC) >= 0`
2. `Adjusted p-value < 0.1`

## Page links
- [What are DEGs?]({{ site.baseurl }}/docs/differentially-expressed-gene/){: .btn}
- [List of DEGs - L2 vs. L1]({{ site.baseurl }}/docs/deg-l2l1/){: .btn}

## Relevant Excel files
[Excel files (Downloads page)]({{ site.baseurl }}/docs/downloads/#9-excel-files-for-degs-dmcs-and-dmgs){: .btn} contain more information than the list presented here.

{% capture excel %}
- Dataset_02_DEG_L3L1.xlsx
{% endcapture %}

<div class="notice">
  {{ excel | markdownify }}
</div>

## List of DEGs between L1 and L3 diets

{% include datatable.html id=page.datatable.id
  data=site.data.deg.degl3l1 nrow=page.datatable.nrow
  nowrap=page.datatable.nowrap %}
