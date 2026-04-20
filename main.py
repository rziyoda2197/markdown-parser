import re

class MarkdownParser:
    def __init__(self, markdown_text):
        self.markdown_text = markdown_text

    def parse(self):
        # Bold text
        bold_pattern = r'\*\*(.*?)\*\*'
        bold_matches = re.findall(bold_pattern, self.markdown_text)
        for match in bold_matches:
            self.markdown_text = self.markdown_text.replace(f'**{match}**', f'<b>{match}</b>')

        # Italic text
        italic_pattern = r'\*(.*?)\*'
        italic_matches = re.findall(italic_pattern, self.markdown_text)
        for match in italic_matches:
            self.markdown_text = self.markdown_text.replace(f'*{match}*', f'<i>{match}</i>')

        # Headers
        header_pattern = r'#(.*?)\n'
        header_matches = re.findall(header_pattern, self.markdown_text)
        for i, match in enumerate(header_matches):
            self.markdown_text = self.markdown_text.replace(f'# {match}\n', f'<h{i+1}>{match}</h{i+1}>')

        # Links
        link_pattern = r'\[(.*?)\]\((.*?)\)'
        link_matches = re.findall(link_pattern, self.markdown_text)
        for match in link_matches:
            self.markdown_text = self.markdown_text.replace(f'[{match[0]}]({match[1]})', f'<a href="{match[1]}">{match[0]}</a>')

        return self.markdown_text

# Test
markdown_text = """
# Heading
This is a **bold** text and this is an *italic* text.
[Link](https://www.example.com)
"""
parser = MarkdownParser(markdown_text)
print(parser.parse())
