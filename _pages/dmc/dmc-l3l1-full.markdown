---
permalink: /docs/dmc-l3l1-full/
layout: splash
title:  "Differentially methylated CpG sites - L3 vs. L1 (full list)"
categories: dna-methylation dmc l3l1
datatable:
  id: dmcl3l1
  nrow: 26995
  nowrap: "Q-value"
---

# {{ page.title }}

## List of the DMCs between L1 and L3 diets

{% include datatable.html id=page.datatable.id
  data=site.data.dmc.dmcl3l1 nrow=page.datatable.nrow
  nowrap=page.datatable.nowrap %}
