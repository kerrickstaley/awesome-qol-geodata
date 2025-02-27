# Awesome Quality of Life Geodata
A curated list of geospatial datasets that allow you to compare the quality of life in different places.

I used some of these datasets when building [NestCB](https://github.com/kerrickstaley/NestCB), a cost/benefit analysis tool to help you decide where to live based on the utility you assign to various factors. In building NestCB I found that one of the hardest parts was locating quality data sources and getting data from them.

See the [code](code) directory for Python code samples showing how to load data from the below sources.

Contributions to this list are warmly welcome; please submit a pull request :)

- [Awesome Quality of Life Geodata](#awesome-quality-of-life-geodata)
  - [Cost of Living / Housing](#cost-of-living--housing)
    - [Zillow Housing Data](#zillow-housing-data)
  - [Weather / Climate](#weather--climate)
    - [NOAA ISD](#noaa-isd)
  - [Greenspace / Access to Nature / Parks](#greenspace--access-to-nature--parks)
    - [ParkScore](#parkscore)
  - [Walkability / Bikeability / Transit](#walkability--bikeability--transit)
    - [Walk Score](#walk-score)
  - [Air polution](#air-polution)
    - [EPA AQS](#epa-aqs)
    - [AQICN](#aqicn)
  - [Climate Change](#climate-change)
    - [Hsiang et al. 2017](#hsiang-et-al-2017)
  - [Dating](#dating)
    - [US Census Geographic Comparison Tables](#us-census-geographic-comparison-tables)
    - ["Undressed: This is What Dating Culture Looks Like Across the US" blog post by OKCupid](#undressed-this-is-what-dating-culture-looks-like-across-the-us-blog-post-by-okcupid)
  - [Related stuff](#related-stuff)
    - [City quality of life indices on Wikipedia](#city-quality-of-life-indices-on-wikipedia)
    - [highspeedinternet.com's Best U.S. Cities to Live and Work Remotely](#highspeedinternetcoms-best-us-cities-to-live-and-work-remotely)
    - [nomads.com](#nomadscom)

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

## Dating
### [US Census Geographic Comparison Tables](https://www.census.gov/acs/www/data/data-tables-and-tools/geographic-comparison-tables/)
Many demographic metrics at city, county, and state aggregation levels. [Ratio of Unmarried Men 15 to 44 Years Per 100 Unmarried Women 15 to 44 Years (CSV download)](https://www2.census.gov/programs-surveys/acs/data/2023/1_year_geographic_comparison_tables/GCT1203.csv) is relevant. *US-only*.

### ["Undressed: This is What Dating Culture Looks Like Across the US" blog post by OKCupid](https://theblog.okcupid.com/undressed-this-is-what-dating-culture-looks-like-across-the-us-ef46e8429b0a)
Data about dating app behavior by OKCupid users in several large US cities. Data is from 2017 and only covers select cities, so not quite "awesome". *US-only*

## Related stuff
### [City quality of life indices on Wikipedia](https://en.wikipedia.org/wiki/City_quality_of_life_indices)
List of lists of the best cities in the world to live in according to various sources. *Global*

### [highspeedinternet.com's Best U.S. Cities to Live and Work Remotely](https://www.highspeedinternet.com/best-cities-to-live-work-remotely)
Rates US cities on 13 quantitative factors such as internet speed, population density, and traffic. It allows you to select which factors are important to you and ranks cities based on your selections. *US-only*

### [nomads.com](https://nomads.com/)
Site targeted at digital nomads. Helps nomads decide where to move to. Rates cities on many factors, and has extensive search filters for paying members. Membership is $100. Note: I don't personally use this site, and [people on Reddit seem to think the paid version isn't worthwhile](https://www.reddit.com/r/digitalnomad/comments/1fnfayp/is_nomadscom_worth_the_100_fee/). *Global*
