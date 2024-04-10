import pdfplumber
import json


def extract_information_and_tables(pdf_path: str) -> dict:
    """Extract both text and table data from each page of the PDF document."""
    extracted_data = {
        "text": [],  # Store extracted text
        "tables": []  # Store extracted tables as lists of dictionaries
    }

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # Extract text from the page
            text = page.extract_text()
            extracted_data["text"].append(text)

            # Extract table data from the page
            tables = []
            for table in page.extract_tables():
                # Process table data into dictionaries
                table_data = []
                headers = table[0]
                for row in table[1:]:
                    row_dict = {}
                    for idx, cell in enumerate(row):
                        row_dict[headers[idx]] = cell
                    table_data.append(row_dict)
                tables.append(table_data)
            extracted_data["tables"].append(tables)

    return extracted_data


def save_extracted_data(data: dict, output_file: str):
    """Save the extracted data to a JSON file."""
    # TODO: Implement saving logic to write the `data` dict to the specified `output_file` in JSON format
    try:
        with open(output_file, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Extracted data saved to '{output_file}' successfully.")
    except IOError:
        print(f"Error: Unable to write data to file '{output_file}'.")


def main():
    pdf_path = 'input.pdf'  # TODO: Specify the path to the input PDF file
    output_file = 'output1.json'  # TODO: Specify the path to the output JSON file

    # Extract data from PDF
    extracted_data = extract_information_and_tables(pdf_path)

    # Save the extracted data
    save_extracted_data(extracted_data, output_file)

    print(f"Extracted data has been saved to {output_file}")


if __name__ == "__main__":
    main()
