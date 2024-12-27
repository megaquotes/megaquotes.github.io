import os
from datetime import datetime

# Function to create a Jekyll page from a quote
def write_quote_to_jekyll_page(quote, author, output_directory="_posts"):
    # Get current date in the format required by Jekyll (_posts/YYYY-MM-DD-title.md)
    date_str = datetime.now().strftime("%Y-%m-%d")
    title = f"{author}-{quote[:10]}"  # Use author and the first 10 characters of the quote for the title
    filename = f"{date_str}-{title}.md"  # Format the filename in Jekyll format
    
    # Create the content for the Jekyll page
    content = f"""---
layout: post
title: "{author} - {quote[:10]}"
date: {date_str} 12:00:00 -0000
author: {author}
quote: "{quote}"
---

{quote}

- {author}
"""

    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)
    
    # Write the content to a markdown file
    file_path = os.path.join(output_directory, filename)
    with open(file_path, "w") as file:
        file.write(content)
    
    print(f"Quote written to {file_path}")
"""
# Example usage
quote = "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment."
author = "Buddha"

write_quote_to_jekyll_page(quote, author)
"""
