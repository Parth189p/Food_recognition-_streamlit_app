# 🍽️ Food Recognition – F0 Project

This project is a **Food Recognition System** powered by computer vision and deep learning. It classifies 66 unique food items using a trained model and provides an intuitive **Streamlit web interface** for real-time predictions.

---

## 🚀 Features

- ✅ Recognizes 66 different food classes
- 🖼️ Upload an image and get instant predictions
- 📊 View class probabilities
- 🌐 Simple web app interface using Streamlit

---

## 🧠 Model Overview

The model is trained to classify the following food types:

<details>
<summary>Click to expand 66 supported classes</summary>

| Class Name              | Class Name                   | Class Name                   | Class Name                 |
|-------------------------|------------------------------|------------------------------|----------------------------|
| Apple                   | Artichoke                    | Balaleet                     | Bamya                      |
| Banana                  | Basbousa                     | Bell pepper                  | Broccoli                   |
| Burger                  | Carrot                       | Crab                         | Cucumber                   |
| Dajaj_Mahshi            | Dates_with_tahini            | Fattoush                     | Fries                      |
| Gers_Ogaily             | Grape                        | Harees                       | Hummus                     |
| Jireesh                 | Kebab                        | Kubba                        | Labneh                     |
| Lentil_soup             | Lentil_stew                  | Lobster                      | Luqaimat                   |
| Majboos_Dajaj           | Mallooba(Maqluba)            | Modas_rice                   | Molokhia                   |
| Muhammara               | Murabyan                     | Musakhan_Chicken             | Orange (fruit)             |
| Oyster                  | Peach                        | Pear                         | Pineapple                  |
| Pizza                   | Plain_white_rice             | Pomegranate                  | Potato                     |
| Pumpkin                 | Radish                       | Red_tea_with_mint_or_saffron | Saffron                    |
| Samosa                  | Sandwich                     | Shrimp                       | Strawberry                 |
| Tabouleh                | Taco                         | Tahini                       | Tamarind_juice             |
| Tamria(Tamriyeh)        | Tea_with_milk                | Warak_Enab                   | Watermelon                 |
| Zaatar                  | bread                        | khabeesa                     | laban_drink                |
| om_ali                 | rice_with_meat               |                              |                            |

</details>

---


## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/food-recognition.git
cd food-recognition
```
```
# (Optional) Create and activate a virtual environment
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

```
# Install dependencies
pip install -r requirements.txt
```

```
# Run streamlit app
streamlit run your_app_name.py --server.fileWatcherType none
```