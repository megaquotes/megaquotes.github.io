import openai
import os
from datetime import datetime
from typing import List
from pydantic import BaseModel
from openai import OpenAI


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Ensure the API key is set in your environment

class Author(BaseModel):
    name: str

class AuthorCollection(BaseModel):
    authors: List[Author]

class Quote(BaseModel):
    text: str
    author: str 

class QuoteCollection(BaseModel):
    quotes: list[Quote]

def get_buddhist_quotes():
    # Make the API call to OpenAI's chat completion endpoint
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "I need some buddhist quotes."},
            {"role": "system", "content": "Dont repeat quotes."},
            {"role": "user", "content": "I need 50 buddhist quotes."},
        ],
        response_format=QuoteCollection,
    )

    # Get the response content properly (fixing the TypeError)
    response_content = completion.choices[0].message.parsed
    return response_content


def get_author_quotes(author):
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "I need some quotes from the following authors."},
            {"role": "system", "content": "Dont repeat quotes."},
            {"role": "user", "content": f"I need up to 2  quotes from the author, {author}"},
        ],
        response_format=QuoteCollection,
    )

    # Get the response content properly (fixing the TypeError)
    response_content = completion.choices[0].message.parsed
    return response_content

def get_authors_quotes(authors):
    all_quotes={}
    for author in authors:
        print(f"Getting quotes for {author.name}")
        quotes=get_author_quotes(author.name)
        all_quotes[author.name]=quotes

    return all_quotes


def get_buddhist_authors():
    # Make the API call to OpenAI's chat completion endpoint
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "I need a list of people associated with buddhism"},
            {"role": "system", "content": "Dont repeat people."},
            {"role": "user", "content": "I need 4 people who have written, spoken, or communicated directly on buddhism"},
        ],
        response_format=AuthorCollection,
    )

    # Get the response content properly (fixing the TypeError)
    response_content = completion.choices[0].message.parsed
    return response_content


def get_subject_authors(subject):
    # Make the API call to OpenAI's chat completion endpoint
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"I need a list of people associated with {subject}"},
            {"role": "system", "content": "Dont repeat people."},
            {"role": "user", "content": f"I need 4 people who have written, spoken, or communicated directly on {subject}"},
        ],
        response_format=AuthorCollection,
    )

    # Get the response content properly (fixing the TypeError)
    response_content = completion.choices[0].message.parsed
    return response_content



from genpage import *

# Call the function to write the quote to a Jekyll page

def write_quote_collection(collection, subject="unknown"):
    for quote in collection:
        write_quote_to_jekyll_page(subject, quote.text, quote.author)
        create_author_index(quote.author, subject, description="No Description" )
        create_subject_index(subject)

def write_subject(subject):
    authors=get_subject_authors(subject).authors
    #authors=get_buddhist_authors().authors
    print (type(authors))
    if authors:
        print("Subject Authors:", len(authors))
        print('*'*40)
        for author in authors:
            print(author.name)
    else:
        print("Failed to retrieve valid authors.")
        return

    quotes=get_authors_quotes(authors)
    for k,v in quotes.items():
        print(quotes[k].quotes)
        write_quote_collection(quotes[k].quotes, subject=subject)


# Main function to execute the script and print the results
def main():
    subjects=["buddhism", "science", "computers", "politics", "farming", "nature"]
    for subject in subjects:
        print("subject...",subject)
        write_subject(subject)
    
if __name__ == "__main__":
    main()
