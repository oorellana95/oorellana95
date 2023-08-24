import re
from settings import START_COMMENT, END_COMMENT, LIST_REGEX, README_PATH
from services.credly import Credly
from services.file import get_file, upgrade_file


if __name__ == "__main__":
    credly_badges = Credly()
    md_badges=credly_badges.get_markdown()
    readme = get_file(path=README_PATH)

    """Generate a new Readme.md"""
    if md_badges:
        badges_in_readme = f"{START_COMMENT}\n{md_badges}\n{END_COMMENT}"
        new_content = re.sub(LIST_REGEX, badges_in_readme, readme)
        upgrade_file(path=README_PATH, content=new_content)
    