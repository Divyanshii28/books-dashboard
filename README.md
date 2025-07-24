# 📚 Books Data Analysis Dashboard

This project is a Streamlit web application for exploring and analyzing a dataset of books. The dataset includes attributes such as title, description, price, rating, availability, and category for each book. Users can interactively explore the data through charts, filters, and a sortable data table.

---



---

## 🌐 Features

* Category-based filtering of books
* Interactive visualizations:

  * Bar chart of book count by category
  * Histogram of price distribution
  * Histogram of star ratings
* Top-rated books list
* Expandable raw data table view

---

## 📚 Dataset Information

* **Source:** books.toscrape.com (scraped data)
* **Format:** JSON (`Books.json`)
* **Fields:**

  * `title`, `category`, `price`, `stars`, `availability`, `description`, `url`, `upc`, etc.

---

## 📊 Key Insights

| Insight Area        | Summary                                                  |
| ------------------- | -------------------------------------------------------- |
| Category Spread     | Poetry, YA, Fiction dominate; Politics, Travel underused |
| Star Ratings        | Skewed toward 5 stars; many 1-star books present         |
| Pricing             | Affordable range (₹20–₹55); avg ₹45                      |
| Top Rated Books     | Many 5-star books are low-priced and well-stocked        |
| Inventory Levels    | Uniform; not based on performance                        |
| Description Quality | Better descriptions often lead to better ratings         |

Full insights are documented in `Books Data Insights.md`

---

## ⚙️ Installation & Usage

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/books-dashboard.git
cd books-dashboard
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
books-dashboard/
├── app.py                # Streamlit app
├── Books.json            # Dataset
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── Books Data Insights.md # Detailed analysis report
```


---

## ✍️ Author

**Divyanshi**
*Developed using Streamlit, Python, and Data Visualization Libraries.*

---


