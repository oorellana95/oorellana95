
def get_file(path):
    with open(path, encoding='utf-8') as f:
        readme = f.read()
        f.close()
    return readme

def upgrade_file(path, content):
    with open(path, "w") as f:
        readme = f.write(content)
        f.close()
    return readme