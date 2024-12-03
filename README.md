# 📚 Final Group Project: **Book Scraper**
Book Scraper is a Python tool for extracting book information from [Books to Scrape](https://books.toscrape.com/). It offers robust filtering, sorting, and data manipulation features, including pintegration with Google Sheets for easy data export.

## 📖 Table of Contents
- [Introduction](#-🌟-introduction)
- [Features](#✨-features)
- [Installation](#⚙️-installation)
- [Usage](#🚀-usage)
- [Technical Details for Google Sheets](#📝-technical-details-for-google-sheets)
- [Testing](#🧪-testing)
- [Contributing](#🤝-contributing)

## 🌟 Introduction
**Book Scraper** is a command-line tool designed to scrape and process book data. You can:

- Extract detailed information about books.
- Apply filters such as rating, price, and availability.
- Sort results dynamically.
- Export data to **Google Sheets** or save it as a **JSON** file.

For a complete list of options, refer to the [Usage](#🚀-usage) section.

## ✨ Features
- Scrape books from [Books to Scrape](https://books.toscrape.com/).
- Filter results by:
  - **Availability**
  - **Rating**
  - **Price**
- Sort results by:
  - Title (Ascending/Descending)
  - Rating
  - Availability
- Search for books:
  - By title
  - Using keywords in descriptions
- Export data to:
  - **Google Sheets**
  - **JSON** files for local storage.

## ⚙️ Installation
### Prerequisites:
- Python 3.10+
- pip (Python package manager)
### Steps:
1. Clone the repository:

```
git clone https://github.com/your-username/book-scraper.git
cd BooksScraper
```

2. Create a virtual environment:

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Set up Google Sheets API credentials. Refer to the [Technical Details for Google Sheets](#📝-technical-details-for-google-sheets) section.

## 🚀 Usage
Run **Book Scraper** with various options:

```
python main.py -b <number_of_books> -g <genre> -f <filters> -s <sort_order>
```

### Examples:
1. Scrape 50 books in the Science genre, sorted by rating:

```
python main.py -b 50 -g Science -s "rating ascending"
```

2. Filter by rating and availability:

```
python main.py -b 24 -f "rating < 3, available > 10"
```

3. Search by title:

```
python main.py -g Classics -t "Book Title"
```

For detailed help:

```
python main.py -h
```

## 📝 Technical Details for Google Sheets
### Setup:
1. Enable the Google Sheets API:
   - Follow this guide to enable the API.
2. Create service account credentials:
   - Save the JSON key file (e.g., gsheets-credentials.json).
3. Set the environment variable:

```
export GOOGLE_SHEETS_KEY=/path/to/gsheets-credentials.json
```

_(On Windows, use set instead of export.)_ 

### Export Data:
After scraping, use the following function to write data to a Google Sheet:

```
GoogleSheetsHandler.write_to_worksheet(scraped_books)
```

Ensure you configure **SAMPLE_SPREADSHEET_ID** within the script to point to your Google Sheet.

## 🧪 Testing
Run the unit tests to validate functionality:

```
python -m unittest test_book_scraper.py
```

This will test key components like:

- BookScraper functionality
- Command-line argument parsing
- Google Sheets integration

## 🤝 Contributing
We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch:

```
git checkout -b feature/my-feature
```

3. Commit your changes and submit a pull request.

Ensure your code adheres to [PEP 8](https://pep8.org/) standards and includes appropriate documentation.

## 📧 Contact
For issues, suggestions, or feedback, feel free to open an issue or contact us directly.
