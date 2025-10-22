# Copy & Paste Chunk of File Names into Here
# ⤵
folder_chunk = '''One
Two
Three
'''

def folder_list(folder_chunk):
    lines = folder_chunk.splitlines()
    result = ', '.join(['"{}"'.format(line) for line in lines])
    return result

listed_papers = folder_list(folder_chunk)
print("[" + listed_papers + "]")
