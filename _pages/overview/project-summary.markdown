---
permalink: /docs/project-summary/
layout: single
sidebar:
  nav: "docs"
toc: true
toc_sticky: true
comments: true
share: true
title:  "Project summary"
categories: summary
---

Project summary of NutrEpi WP1 (Gonad).

## Objective
The primary goal of the project is to elucidate potential inter-generational effects induced by micronutrients (vitamins and minerals) through the male germ line of Atlantic salmon.

## Feeding trial
Our analyses were based on the male gonad samples of Atlantic salmon fed with three graded levels of micronutrient supplementation. The main outcome of the feeding trail was summarised in [Vera et al., 2020](https://doi.org/10.1016/j.aquaculture.2020.735551).

### Experimental design
We collected male gonad samples at the final harvest stage for gene expression and DNA methylation analysis.

{% include figure
  image_path="/assets/images/growth/experimental_design.svg"
  alt="Experimental design"
  caption="Three groups of Atlantic salmon were fed with different levels of micronutrients through the trial." %}

### Experimental feed
Through the trial, Atlantic salmon in triplicate groups - L1, L2, L3 - were fed with graded levels of micronutrient supplements, formulated with nutrition package (NP).

{% capture feed %}
- **L1**: 100% NP (recommended composition of micronutrients)
- **L2**: 200% NP
- **L3**: 400% NP
{% endcapture %}

<div class="notice">
  {{ feed | markdownify }}
</div>

{% include table.html id='table_trial_feed' data=site.data.growth.feed
   caption='Added micronutrient concentrations (mg/kg) within the NP.' %}

### Growth performance

{% capture growth1 %}
- **Smolt**: L2 showed the best growth followed by L3
- **Harvest**: Both L2 and L3 showed significantly better growth
{% endcapture %}

<div class="notice">
  <h4 class="no_toc">Body weights</h4>
  {{ growth1 | markdownify }}
</div>

{% capture growth2 %}
- **Smolt**: L1 had a significantly higher HSI than L2 and L3
- **Harvest**: No significant difference among L1, L2 and L3
- `HSI = (Liver weight (g) / Fish weight (g)) × 100`
{% endcapture %}

<div class="notice">
  <h4 class="no_toc">Hepatosomatic index (HSI)</h4>
  {{ growth2 | markdownify }}
</div>

{% capture growth3 %}
- **Harvest**: Fish with overgrown gonad (GSI >0.2%) were excluded
- `GSI = (gonad weight (g) / body weight (g)) * 100`
{% endcapture %}

<div class="notice">
  <h4 class="no_toc">Gonadosomatic index (GSI)</h4>
  {{ growth3 | markdownify }}
</div>

<figure class="half">
    <img src="{{ site.baseurl }}/assets/images/growth/weight_barplot.svg" alt="Barplot of Atlantic salmon body weights">
    <img src="{{ site.baseurl }}/assets/images/growth/hsi_barplot.svg" alt="Barplot of Atlantic salmon hepatosomatic index values">
    <figcaption>Body weights and HSI at smolt and final harvest stages.</figcaption>
</figure>

## Main findings of NutrEpi WP1 (ganad)

{% capture res1 %}
- **Overall diet effect**: both medium (L2) and high (L3) doses of micronutrient supplementation affect gene expression in male gonad. The L3 diet influences more genes than the L2 diet.
- **Male liver samples**: both L2 and L3 diets affect more genes and biological pathways in male liver compared to male gonad.
{% endcapture %}

<div class="notice--info">
  <h4 class="no_toc">1. Gene expression</h4>
  {{ res1 | markdownify }}
</div>

{% capture res2 %}
- **Overall diet effect**: clustering analysis shows a clear separation of L2 and L3 from L1 in the regions around transcription start sites (TSSs), specifically between 1000 bp upstream in promoters and 150 bp downstream in exons.
- **Affected pathways**: micronutrient supplements significantly affect biological pathways related with signalling.
{% endcapture %}

<div class="notice--info">
  <h4 class="no_toc">2. DNA methylation</h4>
  {{ res2 | markdownify }}
</div>

{% capture res3 %}
- Micronutrient supplements significantly *hypo-methylate* CpG sites in the promoter region of <i>glutamate receptor ionotropic, NMDA 3A-like</i> (<i>grin3a-like</i>).
- This differentially methylated region of <i>grin3a-like</i> is targeted by <i><histone deacetylase 2</i> (<i>HDAC2</i>) and a zinc finger protein.
- <i>HDAC2</i> is an enzyme responsible for the removal of acetyl groups from the core histones.
- DNA methylation in <i>grin3a-like</i> together with <i>HDAC2</i> is potentially involved in intergenerational epigenetic inheritance that affects early cell development stages in offspring.
{% endcapture %}

<div class="notice--info">
  <h4 class="no_toc">3. Inheritance of DNA methylation in <i>grin3a-like</i></h4>
  {{ res3 | markdownify }}
</div>

To summarise, this project suggests that DNA methylation of <i>grin3A-like</i> together with <i>hdac2</i> could be a strong candidate for studying intergenerational epigenetic inheritance that affects early cell development stages in offspring. The project also provides extensive data sources for future work.

## Page links
- [Gene expression]({{ site.baseurl }}/docs/gene-expression/){: .btn}
- [DNA methylation]({{ site.baseurl }}/docs/dna-methylation/){: .btn}
