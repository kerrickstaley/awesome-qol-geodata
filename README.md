# Awesome Quality of Life Geodata
A curated list of geospatial datasets that allow you to compare the quality of life in different places.

I used some of these datasets when building [NestCB](https://github.com/kerrickstaley/NestCB), a cost/benefit analysis tool to help you decide where to live based on the utility you assign to various factors. In building NestCB I found that one of the hardest parts was locating quality data sources and getting data from them.

See the [code](code) directory for Python code samples showing how to load data from the below sources.

Contributions to this list are warmly welcome; please submit a pull request :)

## Cost of Living / Housing
### [Zillow Housing Data](https://www.zillow.com/research/data/)
Cost of housing in various cities around the United States. Includes both renting and buying data, for homes of different sizes. *US-only*

## Weather / Climate
### [NOAA ISD](https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database)
Weather observations from stations all around the world, collected hourly, plus aggregated summaries. Most easily accessed through [Amazon's mirror of the dataset](https://aws.amazon.com/marketplace/pp/prodview-tmvgq72wrnzpq). *Global*

## Greenspace / Access to Nature / Parks
### [ParkScore](https://www.tpl.org/parkscore/rankings)
Rates the quality of public parks in the most populous 100 US cities on a scale of 0 to 100 based on several factors. *US-only*.

## Walkability / Bikeability / Transit
### [Walk Score](https://www.walkscore.com/)
Rates the walkability, bikeability, and transit-friendliness of cities on a scale of 0 to 100 based on a propriety analysis. Data available through a free API. Walkability is *Global*, bikeability and transit-friendliness are *US-only*.

## Air polution
### [EPA AQS](https://www.epa.gov/aqs)
Gives annual air quality summary statistics (mean, 95th percentile, etc.) at many sites around the US. Somewhat unreliable, a little difficult to navigate, and seems to have rate-limiting, so not truly "awesome". See code example. *US-only*

### [AQICN](https://aqicn.org/data-platform/register/)
Gives daily PM2.5, PM10, ozone, nitrogen dioxide, sulfur dioxide, and carbon monoxide readings at many sites around the world. Datasets must be manually downloaded (there is a captcha), so not truly "awesome".  (Scroll down to "Free downloadable united database" on the page.) *Global*

## Climate Change
### [Hsiang et al. 2017](https://www.science.org/doi/epdf/10.1126/science.aal4369)
Estimates the future economic impact of climate change in the United States by 2090, per county, as a percentage of each county's current GDP. [CSV with data is here](http://impactlab.org/wp-content/uploads/2023/03/county_damages_by_sector.csv); see "Total damages (% county income)" column. *US-only*

## Related stuff
### [City quality of life indices on Wikipedia](https://en.wikipedia.org/wiki/City_quality_of_life_indices)
List of lists of the best cities in the world to live in according to various sources. *Global*

### [highspeedinternet.com's Best U.S. Cities to Live and Work Remotely](https://www.highspeedinternet.com/best-cities-to-live-work-remotely)
Rates US cities on 13 quantitative factors such as internet speed, population density, and traffic. It allows you to select which factors are important to you and ranks cities based on your selections. *US-only*

### [nomads.com](https://nomads.com/)
Site targeted at digital nomads. Helps nomads decide where to move to. Rates cities on many factors, and has extensive search filters for paying members. Membership is $100. Note: I don't personally use this site, and [people on Reddit seem to think the paid version isn't worthwhile](https://www.reddit.com/r/digitalnomad/comments/1fnfayp/is_nomadscom_worth_the_100_fee/). *Global*
