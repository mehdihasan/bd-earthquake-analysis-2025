# Assessing the Deadly Earthquake Claim in 🇧🇩

- [Assessing the Deadly Earthquake Claim in 🇧🇩](#assessing-the-deadly-earthquake-claim-in-)
  - [1. Quick analysis overview](#1-quick-analysis-overview)
  - [2. Observations](#2-observations)
  - [3. The four recent incidents — concise assessment](#3-the-four-recent-incidents--concise-assessment)
  - [4. Synthesis — what stands out](#4-synthesis--what-stands-out)
  - [5 Points of concern (operational / hazard implications)](#5-points-of-concern-operational--hazard-implications)
  - [6. Suggested follow-up analyses](#6-suggested-follow-up-analyses)
  - [7. Short summary](#7-short-summary)
  - [8. Limitations \& caveats](#8-limitations--caveats)

## 1. Quick analysis overview

- **Records inside region (Bangladesh bounding box):** **465** events.
- **Time span:** multiple decades (1976–2025) — yearly breakdown printed in the output (example: 2025 → **11** events).
- **Magnitude range (filtered dataset):** mostly in the **~3.5–6.1** band historically; in recent years (2025) magnitudes center ~**4–5.5**.
- **Energy (converted from magnitude):** total seismic energy for **2025 = 2.59×10¹³ J**, versus historical yearly average ≈ **1.57×10¹³ J** (so 2025 is above the long-term mean).
- **Cluster / swarm detection (DBSCAN):** several clusters found (example cluster sizes: **232, 55, 21, 9, 9, 7**). (Note: clustering used scaled spatial+temporal coords; results are sensitive to eps/min_samples.)
- **Filtered “mainshocks” (mag ≥ 5.0):** identified several; found **10 potential aftershock sequences**, including the **2025-11-21 M5.4** event with **2** aftershocks in the 7-day / ±0.5° window.

---

## 2. Observations

- **Yearly counts:** variable; recent years show spikes (e.g., 2021: 24 events; 2023: 19; 2025: 11 so far).

![img](./e_count.png)

- **Magnitude distribution (per-year):**
  - 2025 mean magnitude ~**4.54**, median **4.30**.
  - KS test comparing 2025 magnitudes vs previous years **p = 0.6133** → *no significant change detected in magnitude distribution*.

![img](./mag_distribution.png)

![img](./mag_bin.png)

- **Seismic energy:** 2025 energy (~2.59e13 J) is **~1.65×** the historical yearly average (~1.57e13 J) — indicates energy release this year is above long-term mean.

![img](./seismic_eng_per_yr.png)

- **Depths:**

  - Median depths per year were computed; regression shows **slope = −0.307 km/year, p = 0.001, R² = 0.218**.
    - **Linear regression:** statistically significant decrease in median depth over time (i.e., a **shallowing** trend at ~0.31 km/yr).
    - **Mann–Kendall:** Tau = −0.191, p = 0.066
    → *marginally non-significant* for a monotonic trend (different tests, somewhat divergent result).

    ![img](./median_quake_depth.png)

  - **KS test on depth distributions:** **p = 0.0005**
    → *significant difference* between current-year vs prior years’ depth distribution.
  - **Fraction of shallow events (<40 km):** often high across years; for 2025 it is **1.00** in the output (i.e., all events in 2025 in the filtered set are <40 km).

  ![img](./depth_dis.png)

- **Inter-event times:** median inter-event time: **previous years ≈ 548.6 hours**, **2025 ≈ 652.5 hours**. (So not an increase in event rate in 2025; if anything median inter-event time is longer.)
- **Detection threshold (min mag per year):** improves over decades but in recent years minimum reported in filtered set ~**~3.7–4.1**; for 2025 min mag is **4.0** (so the region's catalog completeness in this filtered dataset appears to assume relatively high cutoff).
- **Statistical tests overall:**
  - **Poisson count test** p ≈ **0.1024** → not significant (no strong evidence that 2025 event count is anomalous relative to historical yearly mean).
  - **KS on magnitudes** p ≈ **0.6133** → magnitudes not significantly different this year vs past.
  - **KS on depths** p ≈ **0.0005** → significant difference in depth distributions (recent events are shallower).

---

## 3. The four recent incidents — concise assessment

Four events of interest (times converted to local UTC timestamps):

|               Time (UTC) |     Lat |     Lon | Depth (km) |       Mag | Place                  |
| -----------------------: | ------: | ------: | ---------: | --------: | ---------------------- |
| 2025-11-21T04:38:28.765Z | 23.8079 | 90.6489 |         27 | 5.4 (mww) | 14 km SSW of Narsingdi |
| 2025-11-22T12:06:05.145Z | 23.9327 | 90.6053 |         10 |  4.3 (mb) | 11 km W of Narsingdi   |
| 2025-11-27T10:15:18.059Z | 24.0897 | 90.4824 |         10 |  4.0 (mb) | 23 km NNE of Tungi     |
| 2025-12-04T00:14:40.379Z | 23.6935 | 90.4716 |         10 |  4.1 (mb) | 6 km ESE of Dhaka      |

**Interpretation:**

- **The 2025-11-21 M5.4** is the largest of the four and appears to be a **mainshock** in time and magnitude. It occurred at shallow depth (27 km) with reasonable location/magnitude quality (table: horizontalError 7.35 km; depthError 1.181 km; magError 0.062; magNst =25).
- The **three November–December M≈4.0–4.3** events are **spatially close** (within ~<50 km) and **temporally follow** the M5.4 (11/22, 11/27, 12/04). All are at **shallow depths (10 km)** in the catalog. Given proximity in space/time and the mainshock magnitude, these are **most plausibly aftershocks** (or part of the same regional activation).  Aftershock search (7-day / ±0.5°) captured 2 aftershocks for the 11/21 mainshock — that aligns with the three events listed (one immediately after on 11/22, two others within ~2 weeks).
- **Implication:** The sequence (M5.4 mainshock → M4.x aftershocks) is consistent with typical aftershock behavior (smaller magnitudes concentrated near mainshock location and shallow depth). The DBSCAN clustering that produced a large cluster near these coordinates further supports local activation.

---

## 4. Synthesis — what stands out

1. **A localized 2025 sequence centered near Narsingdi/Dhaka** is the primary current feature: the M5.4 (2025-11-21) mainshock plus several M≈4 aftershocks in the following days/weeks.
2. **Depths are notably shallow in 2025:** tests show a statistically significant difference in depth distributions this year versus historical (KS p=0.0005). The linear trend test indicates a significant long-term shallowing trend (~0.31 km/yr), though Mann–Kendall is marginal (p≈0.066). Combined, this flags an increase in the proportion of *shallow* events (which matters for surface shaking).
3. **Energy release in 2025 is elevated** relative to the long-term average (≈1.65× average). That primarily reflects the presence of a M5.4 mainshock (energy scales strongly with magnitude).
4. **No clear increase in event count rate** for 2025 (Poisson p≈0.10; median inter-event time actually longer in 2025 than previous years in the subset). So this is more likely a **re-distribution of energy** into a few stronger events rather than a wholesale increase in the number of events.
5. **Clusters / swarms exist** in the catalog (DBSCAN flagged multiple clusters). Interpretation depends on DBSCAN parameters (spatial+temporal scaling; cluster sizes very sensitive to eps and scaling).

---

## 5 Points of concern (operational / hazard implications)

- **Shallower events → greater ground motion at the surface** for a given magnitude. With a statistically significant shift toward shallower depths, even moderate magnitudes (M~4–5) can produce stronger local shaking than if they were deeper. This increases risk for vulnerable structures in the Dhaka/Narsingdi region.
- **Recent M5.4 mainshock** means **aftershock hazard persists** (possibility of M≥4 aftershocks and, rarely, M≥5 aftershocks in the near term). Though the aftershock counts are still modest, aftershock sequences can continue for weeks–months.
- **Large clustering result (cluster size = 232)** may reflect long-term background seismicity or an over-permissive clustering parameter; if that cluster overlaps populated areas, it deserves further checking to see whether it indicates prolonged elevated local activity or is an artifact of parameter choice.
- **Location/horizontal errors for some events** are non-negligible (e.g., horizontalError ~13 km for the 12-04 Dhaka event), so precise source mapping and at-risk-area delineation must account for location uncertainty.

---

## 6. Suggested follow-up analyses

1. **Obtain the full low-magnitude catalog (M<4) for the region** (if available) to better characterize foreshock/aftershock behavior, swarm identification, and b-value estimation. My current filtered dataset’s min mag ~4.0 limits resolution.
2. **Compute Omori-law fits** for aftershock decay (to estimate how quickly aftershock rate will decay) and Gutenberg–Richter b-value for the sequence (to check whether stress regime / b-value is anomalous).
3. **Focal mechanisms / moment tensors** for the M5.4 and larger aftershocks — these tell my fault orientation and likely fault system (strike-slip vs thrust vs normal) and whether the sequence is on a known mapped fault.
4. **InSAR / GPS checks** (if available) to detect any coseismic or post-seismic ground deformation around the mainshock — useful to map ruptured patch and inform hazard.
5. **Sensitivity tests for clustering** — re-run DBSCAN with different eps / time-scaling; consider a pure spatial clustering or space-time ETAS modeling for more robust sequence attribution.
6. **Quantify uncertainty** more explicitly — use the reported horizontalError / depthError / magError fields to propagate location/magnitude uncertainty into hazard mapping.
7. **Damage & felt reports collection** (via local agencies / social media / PAGER-like products) to assess real-world impact and validate shaking intensity estimates.

---

## 7. Short summary

A **M5.4 shallow mainshock on 2025-11-21 near Narsingdi** generated several M≈4 aftershocks over the following two weeks; the catalog analysis shows **2025 has above-average seismic energy** and a **significant difference in depth distribution (shallower)** compared with prior years. Event counts are not anomalously high, but **the shallower depths raise concern about local ground shaking and damage vulnerability** — targeted inspections and continued monitoring are recommended.

---

## 8. Limitations & caveats

- This analysis uses a filtered catalog with **minimum magnitudes ≈4**: smaller events (M<4) likely exist but were not included — this reduces resolution of clustering/sequence analysis.
- **Clustering results are parameter sensitive.** DBSCAN on scaled lat/lon/time mixes units — eps/min_samples tuning will change cluster counts and sizes.
- **Different magnitude types (mb, mww, etc.)** were used; small systematic offsets exist between magnitude scales — mixing scales can slightly bias energy sums and magnitude stats.
- **Statistical tests assume independence** and certain conditions; earthquake catalogs violate some assumptions (clustering in time/space). Treat p-values as informative but not definitive.
