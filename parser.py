import requests
from bs4 import BeautifulSoup

# title = 'Four Thousand Weeks-Notebook'
title = "pragmatic"

CLASSES = ["noteText", "sectionHeading"]

def read_html(title):
    html_file = f"./inputs/{title}.html"
    with open(html_file) as fp:
        soup = BeautifulSoup(fp)
    return soup

def get_highlights(title):
    soup = read_html(title)

    with open(f'./outputs/{title}.md', 'w') as writer:
        for tag in soup.find_all(attrs={"class": CLASSES }):
            prefix = '##' if tag.name == 'h2' else '-'
            line = f"{prefix} {tag.contents[0]}\n"
            writer.write(line)

def get_chapters(title):
    soup = read_html(title)

    with open(f'./outputs/chapters_{title}.md', 'w') as writer:
        writer.write("## Chapters\n")
        for element in soup.find_all(attrs={"class": "sectionHeading"}):
            formatted_name = element.text.replace(".", " -")
            chapter = f"- {formatted_name}\n"
            writer.write(chapter)

get_highlights(title)
