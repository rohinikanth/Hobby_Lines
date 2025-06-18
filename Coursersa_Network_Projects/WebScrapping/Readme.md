### 1. Fetched Web Data from Wikipedia

* Accessed an archived Wikipedia page about GDP using the **Wayback Machine**.
* Used `pandas.read_html(url)` to extract all tables from the HTML.

### 2.  Extracted and Selected the Correct Table

* Selected the 4th table from the list using `tables[3]` (indexing starts at 0).
* Loaded it into a DataFrame (`df`) for further processing.

### 3.  Explored the Data

* Viewed the first few rows with `.head()`.
* Checked column names, data types, and general structure using `.columns` and `.info()`.

### 4.   Cleaned the Data

* Renamed and removed unnecessary columns.
* Converted GDP values from string (with commas) to numeric using `pd.to_numeric()` and `str.replace()`.

### 5.  Sorted and Analyzed GDP Data

* Sorted countries by GDP in descending order.
* Reset the index and cleaned up the DataFrame layout for better readability.

### 6.  Exported Cleaned Data

* Saved the cleaned and processed table to a CSV file named `Cleaned_GDP_Data.csv`.

---

