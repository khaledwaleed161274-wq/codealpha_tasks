# ============================================================
# CodeAlpha - Task 3: Task Automation with Python Scripts
# ============================================================

import re

DEFAULT_INPUT = "input_text.txt"
DEFAULT_OUTPUT = "extracted_emails.txt"

EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"


def read_input_file(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{path}' was not found. Create it and add your text first.")
    except PermissionError:
        print(f"Error: No permission to read '{path}'.")
    except UnicodeDecodeError:
        print(f"Error: Could not decode '{path}' as UTF-8 text.")
    except OSError as error:
        print(f"Error: Failed to read '{path}' ({error}).")
    return None


def extract_unique_emails(text):
    matches = re.findall(EMAIL_PATTERN, text)

    unique_emails = []
    seen = set()

    for email in matches:
        normalized = email.lower()
        if normalized not in seen:
            seen.add(normalized)
            unique_emails.append(email)

    return unique_emails, len(matches)


def save_emails_to_file(emails, path):
    try:
        with open(path, "w", encoding="utf-8") as file:
            for email in emails:
                file.write(email + "\n")
        return True
    except PermissionError:
        print(f"Error: No permission to write to '{path}'.")
    except OSError as error:
        print(f"Error: Failed to write to '{path}' ({error}).")
    return False


def main():
    print("=== Email Extractor (Task Automation) ===\n")

    input_path = input(f"Enter input file name [{DEFAULT_INPUT}]: ").strip() or DEFAULT_INPUT
    output_path = input(f"Enter output file name [{DEFAULT_OUTPUT}]: ").strip() or DEFAULT_OUTPUT

    content = read_input_file(input_path)
    if content is None:
        return

    unique_emails, total_matches = extract_unique_emails(content)

    if not unique_emails:
        print("\nNo valid email addresses were found in the file.")
        return

    if not save_emails_to_file(unique_emails, output_path):
        return

    print("\n=== Extraction Summary ===")
    print(f"Total matches found : {total_matches}")
    print(f"Unique emails saved : {len(unique_emails)}")
    print(f"Duplicates removed  : {total_matches - len(unique_emails)}")
    print(f"Output file         : {output_path}\n")

    print("Extracted emails:")
    for idx, email in enumerate(unique_emails, start=1):
        print(f"  {idx}. {email}")


if __name__ == "__main__":
    main()