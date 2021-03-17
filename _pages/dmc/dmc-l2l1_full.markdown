---
permalink: /docs/dmc-l2l1-full/
layout: splash
title:  "Differentially methylated CpG sites - L2 vs. L1 (full list)"
categories: dna-methylation dmc l2l1
datatable:
  id: dmcl3l1
  nrow: 100
  nowrap: "Q-value"
---

# {{ page.title }}

## List of the DMCs between L1 and L2 diets

{% include datatable.html id=page.datatable.id
  data=site.data.dmc.dmcl2l1 nrow=page.datatable.nrow
  nowrap=page.datatable.nowrap %}
