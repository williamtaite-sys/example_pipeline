import ast
import os
import sys

def parse_docstring(docstring):
    """Simple helper to format docstrings for Markdown."""
    if not docstring:
        return "No description provided."
    return docstring.strip()

def generate_markdown_for_file(filepath):
    """Reads a python file and generates markdown documentation."""
    with open(filepath, "r") as f:
        tree = ast.parse(f.read())
    
    filename = os.path.basename(filepath)
    module_name = filename.replace(".py", "")
    
    md_output = [f"# Module: {module_name}\n"]
    
    # Module Docstring
    docstring = ast.get_docstring(tree)
    if docstring:
        md_output.append(parse_docstring(docstring))
        md_output.append("\n")
        
    # Functions
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            md_output.append(f"## Function: `{node.name}`\n")
            func_doc = ast.get_docstring(node)
            md_output.append(parse_docstring(func_doc))
            md_output.append("\n")

    return "\n".join(md_output)

def main():
    """Generates Wiki Home.md from source files."""
    source_dir = "."
    output_dir = "wiki_content"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # List of files to document
    files_to_process = ["hello.py"]
    
    combined_docs = ["# Project Documentation\n\nWelcome to the automatically generated documentation.\n"]
    
    for fname in files_to_process:
        if os.path.exists(fname):
            print(f"Processing {fname}...")
            md = generate_markdown_for_file(fname)
            combined_docs.append(md)
            
            # Write individual page as well
            with open(os.path.join(output_dir, f"{fname.replace('.py', '')}.md"), "w") as f:
                f.write(md)
                
    # Write Home.md
    with open(os.path.join(output_dir, "Home.md"), "w") as f:
        f.write("\n---\n".join(combined_docs))
        
    print(f"Documentation generated in {output_dir}/")

if __name__ == "__main__":
    main()
