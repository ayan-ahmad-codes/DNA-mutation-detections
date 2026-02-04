def read_fasta(file):
    content = file.read().decode("utf-8")
    return "".join(line for line in content.splitlines() if not line.startswith(">"))
