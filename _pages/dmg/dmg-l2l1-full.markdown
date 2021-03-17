---
permalink: /docs/dmg-l2l1-full/
layout: splash
title:  "Differentially methylated genes - L2 vs. L1 (full list)"
categories: dna-methylation dmg l2l1
datatable:
  id: dmgl2l1
  nrow: 9774
---

# {{ page.title }}

## List of the DMGs between L1 and L2 diets

{% include datatable.html id=page.datatable.id
  data=site.data.dmg.dmgl2l1 nrow=page.datatable.nrow
  nowrap=page.datatable.nowrap %}
