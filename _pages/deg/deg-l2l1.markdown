---
permalink: /docs/deg-l2l1/
layout: single
classes: wide
sidebar:
  nav: "docs"
title:  "Differentially expressed genes - L2 vs. L1"
categories: gene-expression deg l2l1
datatable:
  id: degl2l1
  nrow: 6
  nowrap: "Adj p-val"
---

## DEGs for L2:L1
We identified 6 DEGs for L2:L1 when the following criteria were applied and L1 was used as control.
1. `abs(LFC) >= 0`
2. `Adjusted p-value < 0.1`

## Page links
- [What are DEGs?]({{ site.baseurl }}/docs/differentially-expressed-gene/){: .btn}
- [List of DEGs - L3 vs. L1]({{ site.baseurl }}/docs/deg-l3l1/){: .btn}

## Relevant Excel files
[Excel files (Downloads page)]({{ site.baseurl }}/docs/downloads/#13-excel-files-for-degs-dmcs-and-dmgs){: .btn} contain more information than the list presented here.

{% capture excel %}
- Dataset_01_DEG_L2L1.xlsx
{% endcapture %}

<div class="notice">
  {{ excel | markdownify }}
</div>

## List of DEGs between L1 and L2 diets

{% include datatable.html id=page.datatable.id
  data=site.data.deg.degl2l1 nrow=page.datatable.nrow
  nowrap=page.datatable.nowrap %}
