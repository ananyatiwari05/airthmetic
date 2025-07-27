# Fuzzy AQI Estimator: Because Air Deserves Better Math

Not all pollution is black and white—so why treat it that way?  
This Python project brings in the power of **fuzzy logic** to estimate the **Air Quality Index (AQI)** using soft rules, smooth transitions, and data from real Indian cities. We don’t just classify air—we understand it.

## what s happening?

- Loads air quality data (Delhi, 2019)
- Uses **PM2.5**, **PM10**, and **NO₂** as inputs
- Applies **fuzzy inference** (Mamdani method) to generate a **continuous AQI score**
- Outputs a time series graph with **color-coded zones** for Excellent, Good, Moderate, Poor, and Hazardous
- Inspired by actual academic research (included)

## folder structure

```

aqi fuzzy/
├── aqi-fuzzy.py        ← Main fuzzy logic script
├── city\_day.csv        ← Input dataset from Kaggle
├── aqi\_project.pdf     ← Reference research paper

````

## data-set source

- 📍 Kaggle Dataset: [Air Quality Data in India (2015–2020)](https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india)
- File Used: `city_day.csv`
- Filters Applied: **City = Delhi**, **Year = 2019**

## fuzzy and dizzy

- Title: *Fuzzy Based Air Quality Index Estimation*
- Focus: Using fuzzy sets and rules to model AQI under uncertainty
- Implementation: Mirrors the logic in the paper — same pollutants, same inference approach, same love for data fuzziness
- Output: A crisp score between 0–10, because "Poor" and "Hazardous" aren't always enough

## libraries used

| Library         | Role                                   |
|-----------------|----------------------------------------|
| `numpy`         | Crunching the numbers                  |
| `pandas`        | Reading and cleaning the dataset       |
| `matplotlib`    | Plotting trends in style               |
| `scikit-fuzzy`  | The fuzzy logic core (rules & outputs) |

> Tested with Python 3.10. Avoid 3.13+ as `scikit-fuzzy` isn't fully supported yet.

Install everything at once:

```bash
pip install numpy pandas matplotlib scikit-fuzzy
````

## the working

1. Load Delhi AQI data from Kaggle CSV
2. Define fuzzy sets for PM2.5, PM10, and NO₂
3. Create rules like:

   * “If PM2.5 is High AND PM10 is High THEN AQI is Poor”
4. Defuzzify to get a final AQI score (0–10 scale)
5. Plot it over 60 days with category bands so the drama shows

## output

* Trendline of AQI values for 60 days
* Shaded bands:

  * 0–2: Excellent
  * 2–4: Good
  * 4–6: Moderate
  * 6–8: Poor
  * 8–10: Hazardous
* Zoomed-in view to highlight subtle air quality changes
* Sharp, clean plots ready for reports or dashboards

## run it

```bash
python aqi-fuzzy.py
```
