---
title: 'LCIA Formatter'
tags:
  - Python
  - astronomy
  - dynamics
  - galactic dynamics
  - milky way
authors:
  - name: Adrian M. Price-Whelan^[Custom footnotes for e.g. denoting who the corresponding author is can be included like this.]
    orcid: 0000-0003-0872-7098
    affiliation: "1, 2" # (Multiple affiliations must be quoted)
  - name: Author Without ORCID
    affiliation: 2
  - name: Author with no affiliation
    affiliation: 3
affiliations:
 - name: Lyman Spitzer, Jr. Fellow, Princeton University
   index: 1
 - name: Institution Name
   index: 2
 - name: Independent Researcher
   index: 3
date: 13 August 2017
bibliography: paper.bib

# Optional fields if submitting to a AAS journal too, see this blog post:
# https://blog.joss.theoj.org/2018/12/a-new-collaboration-with-aas-publishing
aas-doi: 10.3847/xxxxx <- update this with the DOI from AAS once you know it.
aas-journal: Astrophysical Journal <- The name of the AAS journal.
---

# Summary

Overview and highlight relationship to other ecosystem LCA tools-Sarah

# Statement of need

Life cycle impact assessment (LCIA) methods can be implemented in life cycle assessment (LCA) software to provide impact assessment results for life cycle inventory (LCI) data loaded into the software, but the flows used in these methods must match exactly the flows in the LCI data (add ref). As LCI flows are updated, the impact methods should also be made available, and vice versa, as LCIA method developers update characterization factors, they should be available as soon as possible to work with existing LCI data. The LCIA formatter module this paper describes is a specific solution to take LCIA methods from original providers, map them to an authoritative flow list, and export them in common data formats..

# Structure

The code is written in the Python 3.x language and primarily use the latest pandas package for data storage/manipulation. The code is stored on a USEPA GitHub repository and is available for public access. LCIA methods are created in openLCA JSON-LD formats....

Describe package structure etc. - Ben Y
1. Accesses LCIA methods directly from the source (currently includes excel files and access databases), downloading and saving in a temporary cache
2. Flow names, indicators, characterization factors, and other metadata are compiled in a standard format
3. Adjustments are made as needed to improve consistency between indicators and across methods
-handling duplicate entries for the same flow
-data cleaning: e.g. cleaning string names, adjusting capitalization, formatting of CAS
-supporting non specified secondary contexts where non are provided
4. Parsing midpoints from endpoints within a single source, if necessary
5. Applying flow mapping to FEDEFL
-unit conversion as needed
6. Mapped methods are stored locally as parquet files for future access by LCIAformatter or other tools
7. Optionally, mapped methods can be exportd as JSON-LD format for use in LCA software tools such as openLCA.


# Applied Uses

TRACI2.1 - Sarah

ReCiPe2016 - Ben Y

ImpactWorld+ - Ben M

FEDEFL Inventory Methods - Ben Y
The LCIAformatter generates Life Cycle Inventory Methods based on groups of elementary flows identified in the FEDEFL. For example, an inventory method for energy resource use would represent a summation of all instances of these flows within a dataset. Where necessary unit conversions are applied to achieve a consistent indicator unit. 

Valuation and other Endpoint Methods - Andrew

Current use by other ecosystem tools (i.e. USEEIOr)?


# Conclusions and Future Applications

The system was built to be flexible enough to support creating outputs for LCIA spatially-explicit characterization factors.

Future applications:
-regionalization
-custom methods

# Citations

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:
- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Figures

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Figure sizes can be customized by adding an optional second parameter:
![Caption for example figure.](figure.png){ width=20% }

# Acknowledgements

We acknowledge contributions from Brigitta Sipocz, Syrtis Major, and Semyeong
Oh, and support from Kathryn Johnston during the genesis of this project.

# References