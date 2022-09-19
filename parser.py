from distutils.command.build import build
import requests
from bs4 import BeautifulSoup
import os

FILES = [i for i in os.listdir('./inputs') if i.endswith('.html')]
TITLES = list(map(lambda x: x.replace(".html", ""), FILES))
CLASSES = ["noteText", "sectionHeading"]

def read_html(title):
    html_file = f"./inputs/{title}.html"
    with open(html_file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
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

    with open(f'./outputs/notes_{title}.md', 'w') as writer:
        for tag in soup.find_all(attrs={"class": CLASSES }):
            writer.write(build_line(tag))

def build_line(tag):
    prefix = '  -'
    highlight_text = tag.contents[0]

    if tag.name == 'h2':
        prefix = '-'
        highlight_text = highlight_text.replace(".", " -")

    return f"{prefix} {highlight_text}\n"


for title in TITLES:
    get_highlights(title)
    print(f"Succesfully exported notebook {title}")

for title in TITLES:
    get_chapters(title)
    print(f"Succesfully exported chapter outline for {title}")

# def build_line_with_user_notes(tag):
      # class_type = tag.get('class')[0]
#     # loc = ''
#     note_text = ''
#     line = ''
#     if class_type == 'noteHeading':
#         entry_kind = tag.text.split()[0]
#         # loc = tag.text.split()[-1] if entry_kind == 'Highlight' else ''
#         note_text = tag.text if entry_kind == 'Note' else ''
#         line = f"- {note_text}\n"
#     elif class_type == 'noteText':
#         prefix = '##' if tag.name == 'h2' else '-'
#         highlight = tag.contents[0]
#         line = f"{prefix} {highlight}\n"
#     else:
#         line = ''
#     return line
