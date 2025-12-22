import os
import sys
import subprocess
import google.generativeai as genai

# Configuration
# Ensure you set the GOOGLE_API_KEY environment variable
MODEL_NAME = "gemini-1.5-flash"
SOURCE_DIR = "."
OUTPUT_DIR = "wiki_content"
FILES_TO_PROCESS = ["hello.py", "data_processor.py"]

def git_pull():
    """Pulls the latest changes from the remote repository."""
    print("Pulling latest changes...")
    try:
        subprocess.run(["git", "pull"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error pulling changes: {e}")
        # We continue even if pull fails, as we might be working locally

def generate_docs_for_code(code_content, filename):
    """Uses Gemini to generate documentation for the code."""
    model = genai.GenerativeModel(MODEL_NAME)
    
    prompt = f"""
    You are a technical documentation expert. 
    
    Please write comprehensive documentation in Markdown format for the following Python file named '{filename}'.
    
    Structure the documentation as follows:
    1. **Module Overview**: A high-level summary of what the module does.
    2. **Functions**: For each function, provide:
       - Description
       - Parameters (if any)
       - Return values
       - Usage Example
    
    Here is the code:
    ```python
    {code_content}
    ```
    """
    
    response = model.generate_content(prompt)
    return response.text

def main():
    # 1. Update Repo
    git_pull()

    # 2. Check API Key
    if not os.environ.get("GOOGLE_API_KEY"):
        print("Error: GOOGLE_API_KEY environment variable not set.")
        sys.exit(1)

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    combined_docs = ["# Project Documentation (AI Generated)\n\nWelcome to the AI-generated documentation.\n"]

    # 3. Process Files
    for fname in FILES_TO_PROCESS:
        if os.path.exists(fname):
            print(f"Generating AI docs for {fname}...")
            
            with open(fname, "r") as f:
                code_content = f.read()
            
            try:
                md_content = generate_docs_for_code(code_content, fname)
                
                # Save individual page
                output_path = os.path.join(OUTPUT_DIR, f"{fname.replace('.py', '')}.md")
                with open(output_path, "w") as f:
                    f.write(md_content)
                
                combined_docs.append(md_content)
                
            except Exception as e:
                print(f"Failed to generate docs for {fname}: {e}")

    # 4. Create Home.md
    with open(os.path.join(OUTPUT_DIR, "Home.md"), "w") as f:
        f.write("\n---\n".join(combined_docs))

    print(f"AI Documentation generated in {OUTPUT_DIR}/")
    print("To publish, run your git wiki publish commands or the GitHub Action.")

if __name__ == "__main__":
    main()
