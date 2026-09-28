# Month 1 Summary

## Research Question

Which residential areas in Shimolu are more than 2 km from the nearest emergency healthcare facility, specifically hospitals?

## Operation and Why

I focused the analysis specifically on hospitals as the emergency healthcare facilities of interest. I initially considered a 2 km distance, but after examining the study area, I found that a 2 km buffer was too large for the level of detail required. I therefore adjusted the analysis to a 500 m buffer to provide a more meaningful representation of proximity to hospitals.

I created buffers around the hospital locations and used them to identify residential areas within the specified distance. This provided a straight-line distance between residential areas and hospitals rather than distance based on the actual road network.

## What I Expected and What I Got

I expected the analysis to identify residential areas that were within and beyond the selected distance from hospitals. The resulting buffer showed the areas covered by the hospitals based on straight-line distance.

The analysis was useful for identifying areas of potential healthcare accessibility gaps. However, the results should not be interpreted as actual travel distance because the analysis did not account for roads, routes, barriers, or the distance required to travel from a residential area to a hospital.

## What Surprised Me

There were no major unexpected findings during the analysis. The main observation was that the original 2 km buffer was too large for the study area and did not provide the level of spatial detail I wanted. This led me to revise the distance to 500 m.

## Data I Still Need

One important dataset I still needed was detailed building data within the residential areas. Initially, I only had the residential-area polygon, which was not sufficient for identifying individual buildings that could be affected by the distance from hospitals. I therefore obtained building data and clipped the buildings to the residential-area boundary.

For a more accurate accessibility analysis, I would also need a detailed road network and potentially information on road accessibility and travel routes. The current analysis measures straight-line distance ("as the crow flies"), so incorporating the road network would allow me to calculate actual route-based distances to hospitals.

## Overall Reflection

The first month did not progress as strongly as I had initially hoped, partly because I became distracted during the period. However, the work completed helped me understand the limitations of the initial approach and refine the research question and methodology. I expect to build on this foundation in the coming months, particularly by incorporating the additional datasets and improving the distance analysis.
