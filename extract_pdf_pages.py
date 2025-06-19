import PyPDF2
import os

def extract_pdf_pages(input_path, output_path, start_page, end_page):
    """
    Extract specific pages from a PDF file and save them as a new PDF.
    
    Args:
        input_path (str): Path to the input PDF file
        output_path (str): Path where the output PDF will be saved
        start_page (int): Starting page number (1-indexed)
        end_page (int): Ending page number (1-indexed)
    """
    try:
        # Open the input PDF file
        with open(input_path, 'rb') as input_file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(input_file)
            
            # Get the total number of pages
            total_pages = len(pdf_reader.pages)
            print(f"Total pages in the PDF: {total_pages}")
            
            # Validate page range
            if start_page < 1 or end_page > total_pages or start_page > end_page:
                print(f"Invalid page range. Pages must be between 1 and {total_pages}")
                return False
            
            # Create a PDF writer object
            pdf_writer = PyPDF2.PdfWriter()
            
            # Extract the specified pages (convert to 0-indexed)
            for page_num in range(start_page - 1, end_page):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)
                print(f"Added page {page_num + 1}")
            
            # Write the extracted pages to the output file
            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)
            
            print(f"Successfully extracted pages {start_page}-{end_page} to {output_path}")
            return True
            
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

def main():
    # Define file paths
    input_file = "files/978-3-031-64299-9.pdf"
    output_file = "files/extracted_pages_134_149.pdf"
    
    # Define page range (134 to 149)
    start_page = 164
    end_page = 179
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        return
    
    # Extract the pages
    success = extract_pdf_pages(input_file, output_file, start_page, end_page)
    
    if success:
        print(f"\nExtraction completed successfully!")
        print(f"Output file: {output_file}")
    else:
        print("\nExtraction failed.")

if __name__ == "__main__":
    main() 