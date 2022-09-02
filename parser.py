from distutils.command.build import build
import requests
from bs4 import BeautifulSoup

# title = 'Four Thousand Weeks-Notebook'
title = "test"
CLASSES = ["noteText", "sectionHeading"]

def read_html(title):
    html_file = f"./inputs/{title}.html"
    with open(html_file) as fp:
        soup = BeautifulSoup(fp)
    return soup

def get_chapters(title):
    soup = read_html(title)

    with open(f'./outputs/chapters_{title}.md', 'w') as writer:
        writer.write("## Chapters\n")
        for element in soup.find_all(attrs={"class": "sectionHeading"}):
            formatted_name = element.text.replace(".", " -")
            chapter = f"- {formatted_name}\n"
            writer.write(chapter)

def get_highlights(title):
    soup = read_html(title)

    with open(f'./outputs/{title}.md', 'w') as writer:
        for tag in soup.find_all(attrs={"class": CLASSES }):
            writer.write(build_line(tag))

def build_line(tag):
    prefix = '##' if tag.name == 'h2' else '-'
    highlight_text = tag.contents[0]
    return f"{prefix} {highlight_text}\n"


get_highlights(title)
