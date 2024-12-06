# 📚 Final Group Project: **Book Scraper**
Book Scraper is a Python tool for extracting book information from [Books to Scrape](https://books.toscrape.com/). It offers robust filtering, sorting, and a server-client architecture that allows remote input submission and result processing.

## 📖 Table of Contents
- [Introduction](#-🌟-introduction)
- [Features](#✨-features)
- [Installation](#⚙️-installation)
- [Usage](#🚀-usage)
- [Testing](#🧪-testing)
- [Contributing](#🤝-contributing)

## 🌟 Introduction
**Book Scraper** is a command-line tool designed to scrape and process book data. You can:

- Extract detailed information about books.
- Apply filters such as rating, price, and availability.
- Sort results dynamically.
- Save the data as a **JSON** file.

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
  - **JSON** files for local storage.

### Server-Client Features:
1. The client submits input data (arguments).
2. The server processes the local algorithm using the submitted data.
3. The server returns the results to the client.

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

## 🚀 Usage
### Local Execution:
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

### Server-Client Workflow:
### Steps:
1. Start the server

Run the following command to start the server:
```
python server.py
```
The server will listen on localhost:8080.

2. Submit a client request

Use the client application to send input arguments (e.g., number of books, genre, sort parameters, filter parameters, etc.), just like the local execution. Here is example of client application:

```
python client.py -b 10 -g "Science"
```
3. Receive results

The server processes the request and returns a JSON file with the scraped data:

```
[
    {"title": "Book 1", "author": "Author 1", "genre": "Science", "price": 15.99},
    {"title": "Book 2", "author": "Author 2", "genre": "Science", "price": 20.99}
]
```

## 🧪 Testing
Run the unit tests to validate functionality:

```
python -m unittest test_book_scraper.py
```

This will test key components like:

- BookScraper functionality
- Command-line argument parsing
- Server-client communication

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
