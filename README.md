# 📚 Final Group Project: **Book Scraper**
Book Scraper is a Python tool for extracting book information from [Books to Scrape](https://books.toscrape.com/). It offers robust filtering, sorting, and a server-client architecture that allows remote input submission and dynamic data processing.

## 📖 Table of Contents
- [Introduction](#-🌟-introduction)
- [Features](#✨-features)
- [Installation](#⚙️-installation)
- [Usage](#🚀-usage)
- [Server-Client Workflow](#🌐-server-client-workflow)
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
1. Client submits input data (arguments).
2. Server processes the web scraping algorithm using the submitted data.
3. Client submits number of lines to be returned from the server.
4. Server returns the results to the client.

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

### 🌐 Server-Client Workflow:
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
python client.py -b 2 -g "Fantasy"
```
3. Specify number of entries

The client can request a specific number of book entries by entering a value after the server is started.

```
Enter the number of lines to retrieve from the server: N
```

4. Receive results

The server processes the request and returns a JSON-formatted response containing the requested number of book entries:

```
[
    {
        "title": "Saga, Volume 6 (Saga (Collected Editions) #6)",
        "genre": "Fantasy",
        "price": "£25.02",
        "rating": 3,
        "availability": "In stock (16 available)",
        "description": "After a dramatic time jump, the three-time Eisner Award winner for Best Continuing Series continues to evolve, as Hazel begins the most exciting adventure of her life: kindergarten. Meanwhile, her star-crossed family learns hard lessons of their own.Collects SAGA #31-36"
    },
    {
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
