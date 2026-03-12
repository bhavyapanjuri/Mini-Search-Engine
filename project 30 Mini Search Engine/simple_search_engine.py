import os
import math
from collections import defaultdict

# Stopwords to filter out
STOPWORDS = {'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he', 'in', 'is', 'it', 'of', 'on', 'that', 'the', 'to', 'was', 'will', 'with'}

def process_text(text):
    """Clean and tokenize text"""
    text = text.lower()
    for char in '.,!?;:':
        text = text.replace(char, '')
    words = [w for w in text.split() if w not in STOPWORDS]
    return words

def load_documents(folder):
    """Load all .txt files from folder"""
    if not os.path.exists(folder):
        print(f"Error: Folder '{folder}' does not exist!")
        return None
    
    docs = {}
    for file in os.listdir(folder):
        if file.endswith('.txt'):
            with open(os.path.join(folder, file), 'r', encoding='utf-8') as f:
                docs[file] = f.read()
    
    if not docs:
        print(f"Error: No .txt files found in '{folder}'!")
        return None
    
    return docs

def build_index(documents):
    """Build inverted index"""
    index = defaultdict(dict)
    doc_tokens = {}
    
    for doc_name, content in documents.items():
        tokens = process_text(content)
        doc_tokens[doc_name] = tokens
        
        word_count = defaultdict(int)
        for word in tokens:
            word_count[word] += 1
        
        for word, count in word_count.items():
            index[word][doc_name] = count
    
    return index, doc_tokens

def search(query, index, doc_tokens, documents):
    """Search and rank documents"""
    query_words = process_text(query)
    if not query_words:
        return []
    
    scores = defaultdict(float)
    total_docs = len(documents)
    
    for word in query_words:
        if word in index:
            docs_with_word = index[word]
            idf = math.log(total_docs / len(docs_with_word))
            
            for doc_name, word_count in docs_with_word.items():
                tf = word_count / len(doc_tokens[doc_name])
                scores[doc_name] += tf * idf
    
    results = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    # Add snippets
    output = []
    for doc_name, score in results:
        snippet = documents[doc_name][:100] + "..."
        output.append((doc_name, score, snippet))
    
    return output

def phrase_search(phrase, doc_tokens, documents):
    """Search for exact phrase"""
    phrase_words = process_text(phrase)
    if not phrase_words:
        return []
    
    results = []
    for doc_name, tokens in doc_tokens.items():
        for i in range(len(tokens) - len(phrase_words) + 1):
            if tokens[i:i+len(phrase_words)] == phrase_words:
                snippet = documents[doc_name][:100] + "..."
                results.append((doc_name, 1.0, snippet))
                break
    
    return results

def main():
    print("=" * 60)
    print("MINI SEARCH ENGINE")
    print("=" * 60)
    
    folder = input("\nEnter folder path (default: 'sample_docs'): ").strip() or "sample_docs"
    
    print(f"\nLoading documents from '{folder}'...")
    documents = load_documents(folder)
    
    if documents is None:
        return
    
    print(f"Loaded {len(documents)} documents")
    
    print("\nBuilding index...")
    index, doc_tokens = build_index(documents)
    print(f"Indexed {len(index)} unique words")
    
    print("\n" + "=" * 60)
    print("Enter keywords or \"phrase in quotes\" (type 'exit' to quit)")
    print("=" * 60)
    
    while True:
        query = input("\nSearch: ").strip()
        
        if query.lower() == 'exit':
            print("Goodbye!")
            break
        
        if not query:
            continue
        
        # Check if phrase search
        if query.startswith('"') and query.endswith('"'):
            results = phrase_search(query[1:-1], doc_tokens, documents)
        else:
            results = search(query, index, doc_tokens, documents)
        
        if results:
            print(f"\nFound {len(results)} result(s):\n")
            for i, (doc, score, snippet) in enumerate(results, 1):
                print(f"{i}. {doc} (Score: {score:.4f})")
                print(f"   {snippet}\n")
        else:
            print("\nNo results found.\n")

if __name__ == "__main__":
    main()
