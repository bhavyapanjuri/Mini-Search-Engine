# Mini Search Engine

A simple Python search engine that indexes text files and enables keyword and phrase-based searching with TF-IDF ranking.

## Features

- Document Indexing (Inverted Index)
- Keyword Search
- Phrase Search (exact match)
- TF-IDF Ranking
- Result Snippets
- Single file implementation

## Files

```
Mini_Search_Engine/
├── simple_search_engine.py  # Main program
├── docs/                    # Sample text files
│   ├── file1.txt
│   ├── file2.txt
│   └── file3.txt
└── README.md               # This file
```

## Requirements

- Python 3.7+
- No external dependencies

## Usage

```bash
python simple_search_engine.py
```

**When prompted:**
1. Enter folder path: `docs` (or press Enter for default)
2. Type your search query
3. Type `exit` to quit

### Examples

**Keyword Search:**
```
Search: python programming
```

**Phrase Search:**
```
Search: "machine learning"
```

**Exit:**
```
Search: exit
```

## How It Works

1. **Text Preprocessing**: Lowercase, remove punctuation, filter stopwords
2. **Inverted Index**: Maps words to documents with frequency counts
3. **TF-IDF Ranking**: Calculates relevance scores
   - TF = term frequency in document
   - IDF = inverse document frequency
   - Score = TF × IDF
4. **Search**: Finds and ranks matching documents

## Sample Output

```
============================================================
MINI SEARCH ENGINE
============================================================

Enter folder path (default: 'sample_docs'): docs

Loading documents from 'docs'...
Loaded 3 documents

Building index...
Indexed 67 unique words

============================================================
Enter keywords or "phrase in quotes" (type 'exit' to quit)
============================================================

Search: python

Found 2 result(s):

1. file1.txt (Score: 0.0730)
   Python is a high-level programming language. It is widely used for web development, data science...

2. file3.txt (Score: 0.0365)
   Data science combines statistics, programming, and domain expertise. Data scientists analyze lar...

Search: "machine learning"

Found 2 result(s):

1. file1.txt (Score: 1.0000)
   Python is a high-level programming language. It is widely used for web development, data science...

2. file2.txt (Score: 1.0000)
   Machine learning is a subset of artificial intelligence. It enables computers to learn from data...

Search: exit
Goodbye!
```

## Add Your Own Documents

1. Create a folder (e.g., `my_docs`)
2. Add `.txt` files to the folder
3. Run: `python simple_search_engine.py`
4. Enter your folder path: `my_docs`
5. Start searching!

---

**Built with Python | No dependencies required**
