---
permalink: /docs/dmg-l3l1-full/
layout: splash
title:  "Differentially methylated genes - L3 vs. L1 (full list)"
categories: dna-methylation dmg l3l1
datatable:
  id: dmgl3l1
  nrow: 9647
---

# {{ page.title }}

## List of the DMGs between L1 and L3 diets

{% include datatable.html id=page.datatable.id
  data=site.data.dmg.dmgl3l1 nrow=page.datatable.nrow
  nowrap=page.datatable.nowrap %}
