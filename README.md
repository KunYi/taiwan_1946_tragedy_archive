# The Tragedy of Taiwan (1946) - Digital Archive

This project is a digital preservation and reconstruction initiative for the investigative series **"The Tragedy of Taiwan"**, written by **Harlow M. Church**. The series was originally published in **The Pittsburgh Press** from April 15 to April 18, 1946.

---

## 📌 Historical Context
Published less than a year before the **February 28 Incident (2-28)**, these reports provide a rare and critical Western perspective on the systemic corruption, economic exploitation ("The Big Squeeze"), and social unrest in post-WWII Taiwan during the transition from Japanese colonial rule to the Nationalist (KMT) administration.

Through modern digital techniques, we have reconstructed these historical broadsheets from fragmented image tiles to ensure their accessibility for future historical research and education.

---

## 🙏 Acknowledgments & Credits
We would like to express our deepest gratitude to **[Google News Archive](https://news.google.com/newspapers)**.

This digital preservation project would not have been possible without Google's massive effort to digitize and host historical newspapers. Their service provides an invaluable window into the past, allowing us to rediscover and analyze crucial historical reports like "The Tragedy of Taiwan" that might otherwise have remained buried in physical archives.

---

## 📂 Project Structure
```text
.
├── scripts/                # Python automation tools
│   ├── get_pics.py         # Multi-date image tile scraper
│   └── stitch_pics.py      # Automated image reconstruction engine
├── processed_images/       # High-resolution stitched broadsheets
├── docs/                   # Translations and historical analysis
├── README.md
└── LICENSE                 # MIT License for source code
```

---

## 🛠 Usage

### 1. Requirements

- Python 3.x
- requests library
- Pillow (PIL) library

### 2. Downloading Tiles

To download the original image tiles for a specific date:

```bash
python scripts/get_pics.py April15
```

Available keys: April15, April16, April17, April18.

### 3. Stitching Images

To reconstruct the tiles into full-page broadsheets:

```bash
python scripts/stitch_pics.py
```

Reconstructed images will be saved in the /`processed_images` folder.

---

## 🔎 Viewing Tips
> **IMPORTANT:** The reconstructed newspaper pages are high-resolution.
> To read the fine print, please **Right-click on the image** and select **"Open image in new tab"**, or click the link below each image to access the raw file.

---

## 📄 Content Summary
1. **Part 1 (Apr 15):** [Administrative chaos and the "Out of the frying pan into the fire" sentiment.](processed_images/April15_stitched.jpg)

![Administrative chaos and the "Out of the frying pan into the fire" sentiment.](processed_images/April15_stitched.jpg)

2. **Part 2 (Apr 16):** [Extortion rackets targeting repatriating Japanese and seizure of property.](processed_images/April16_stitched.jpg)

![Extortion rackets targeting repatriating Japanese and seizure of property.](processed_images/April16_stitched.jpg)

3. **Part 3 (Apr 17):** ["The Big Squeeze" - Monopoly over rice, coal, and sugar.](processed_images/April17_stitched.jpg)

!["The Big Squeeze" - Monopoly over rice, coal, and sugar.](processed_images/April17_stitched.jpg)

4. **Part 4 (Apr 18):** [Industrial paralysis and the decay of infrastructure.](processed_images/April18_stitched.jpg)

![Industrial paralysis and the decay of infrastructure.](processed_images/April18_stitched.jpg)

---

## ⚖️ Copyright & Disclaimer

### Content Attribution
- **Original Content:** All newspaper articles, photographs, and clippings archived in this repository are the property of the **Pittsburgh Press** (now owned by **Block Communications**) or the original copyright holders.
- **Fair Use:** This repository is intended for **non-commercial, educational, and historical research purposes only**. The digital reconstruction is provided to facilitate easier access for historians and scholars.
- **Takedown Policy:** If you are the legal copyright holder and object to the inclusion of this material, please contact the maintainer to request removal.

---

### Software License
The Python scripts (`get_pics.py` and `stitch_pics.py`) are original works and are licensed under the **MIT License**. You are free to use and modify the code, provided that credit is given to the author.

---

Dedicated to preserving the historical truth of Taiwan.
