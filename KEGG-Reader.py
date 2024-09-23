# You need to install biopython into your environment.
# (A command like !pip install biopython or conda 
# install -c conda-forge biopython will work.)")

# The format of the function calling should be:
# reader(r"{path}", "{gene name}")\n')

def reader(path, clock_name):
    from Bio.KEGG.KGML.KGML_parser import read
    clock = read(open(path, 'r'))
    input_text = ""
    for item in clock.get_KGML().split("\n"):
        input_text += item + "\n"
    extracted_parts = []
    lines = input_text.strip().split('\n')
    for line in lines:
        start = line.find('"') + 1
        end = line.find(',', start)
        if start != -1 and end != -1:
            extracted_part = line[start:end]
            extracted_parts.append(extracted_part)
    extracted_parts = list(set(extracted_parts))
    print(clock_name, "genes:", ", ".join(extracted_parts) + ".\n")
    print(clock_name, extracted_parts, "\n")